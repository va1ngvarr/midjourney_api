import os
import re
import json
import logging

import requests
import pandas as pd


class Receiver:
    def __init__(self, params, local_path):
        self.local_path = local_path

        if !os.path.isdir(local_path):
            os.mkdir(local_path) 

        self.df = pd.DataFrame(columns=["prompt", "url", "filename", "is_downloaded"])
        self.awaiting_list = pd.DataFrame(columns=["prompt", "status"])

        self.channel_id = params["channel_id"]
        self.authorization = params["authorization"]
        self.headers = {"authorization": self.authorization}


    # Collect all available images to download
    def collecting_all_results(self) -> None:
        r = requests.get(
            f"https://discord.com/api/v10/channels/{self.channel_id}/messages?limit={100}",
            headers=self.headers,
        )

        # Getting last 100 messages as Python-object
        message_list = json.loads(r.text)

        # Collect generated images weren't downloaded from last 100 messages
        for message in message_list:
            if (message["author"]["username"] == "Midjourney Bot") and (
                "**" in message["content"]
            ):
                if len(message["attachments"]) > 0:
                    if (message["attachments"][0]["filename"][-4:] == ".png") or (
                        "(Open on website for full quality)" in message["content"]
                    ):
                        id = message["id"]
                        prompt = message["content"].split("**")[1].split(" --")[0]
                        url = message["attachments"][0]["url"]
                        filename = message["attachments"][0]["filename"]
                        if id not in self.df.index:
                            self.df.loc[id] = [prompt, url, filename, 0]

                    else:
                        id = message["id"]
                        prompt = message["content"].split("**")[1].split(" --")[0]
                        if ("(fast)" in message["content"]) or (
                            "(relaxed)" in message["content"]
                        ):
                            try:
                                status = re.findall("(\w*%)", message["content"])[0]
                            except:
                                status = "unknown status"
                        self.awaiting_list.loc[id] = [prompt, status]

                else:
                    id = message["id"]
                    prompt = message["content"].split("**")[1].split(" --")[0]
                    if "(Waiting to start)" in message["content"]:
                        status = "Waiting to start"
                    self.awaiting_list.loc[id] = [prompt, status]

    # Collect image with certain prompt
    def collecting_result_with_prompt(self) -> None:
        r = requests.get(
            f"https://discord.com/api/v10/channels/{self.channel_id}/messages?limit={100}",
            headers=self.headers,
        )

        # Getting last 100 messages as Python-object
        message_list = json.loads(r.text)

        # Collect generated images weren't downloaded from last 100 messages
        for message in message_list:
            if (message["author"]["username"] == "Midjourney Bot") and (
                "**" in message["content"]
            ):
                if len(message["attachments"]) > 0:
                    if (message["attachments"][0]["filename"][-4:] == ".png") or (
                        "(Open on website for full quality)" in message["content"]
                    ):
                        id = message["id"]
                        prompt = message["content"].split("**")[1].split(" --")[0]
                        url = message["attachments"][0]["url"]
                        filename = message["attachments"][0]["filename"]
                        if id not in self.df.index:
                            self.df.loc[id] = [prompt, url, filename, 0]

                    else:
                        id = message["id"]
                        prompt = message["content"].split("**")[1].split(" --")[0]
                        if ("(fast)" in message["content"]) or (
                            "(relaxed)" in message["content"]
                        ):
                            try:
                                status = re.findall("(\w*%)", message["content"])[0]
                            except:
                                status = "unknown status"
                        self.awaiting_list.loc[id] = [prompt, status]

                else:
                    id = message["id"]
                    prompt = message["content"].split("**")[1].split(" --")[0]
                    if "(Waiting to start)" in message["content"]:
                        status = "Waiting to start"
                    self.awaiting_list.loc[id] = [prompt, status]

    def get_awaiting_list(self) -> int:
        return self.awaiting_list

    # Output separated results
    def outputer(self) -> None:
        if len(self.awaiting_list) > 0:
            logging.info(
                f"Prompts in progress: \n{self.awaiting_list}\n"
                + "====================================================="
            )

        waiting_for_download = [
            self.df.loc[i].prompt
            for i in self.df.index
            if self.df.loc[i].is_downloaded == 0
        ]

        if len(waiting_for_download) > 0:
            logging.info(
                f"Waiting for download prompts: \n{waiting_for_download}\n"
                + "====================================================="
            )

    # Download all availible images to download
    def downloading_all_results(self) -> None:
        processed_prompts = []

        for i in self.df.index:
            if self.df.loc[i].is_downloaded == 0:
                response = requests.get(self.df.loc[i].url)
                with open(
                    os.path.join(self.local_path, self.df.loc[i].filename), "wb"
                ) as req:
                    req.write(response.content)
                self.df.loc[i, "is_downloaded"] = 1
                processed_prompts.append(self.df.loc[i].prompt)

        if len(processed_prompts) > 0:
            logging.info(
                f"Processed prompts: \n{processed_prompts}\n"
                + "====================================================="
            )

    # Download image with certain prompt
    def downloading_result_with_prompt(self, prompt) -> None:
        for i in self.df.index:
            if self.df.loc[i].is_downloaded == 0 and self.df.loc[i].prompt == prompt:
                response = requests.get(self.df.loc[i].url)
                with open(
                    os.path.join(self.local_path, self.df.loc[i].filename), "wb"
                ) as req:
                    req.write(response.content)
                self.df.loc[i, "is_downloaded"] = 1
                processed_prompts.append(self.df.loc[i].prompt)
                break

        if len(processed_prompts) > 0:
            logging.info(
                f"Processed prompts: \n{processed_prompts}\n"
                + "====================================================="
            )
