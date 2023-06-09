import logging
import re

import requests


url = "https://discord.com/api/v9/interactions"


class Sender:
    def __init__(self, params, flags=None):
        self.channel_id = params["channel_id"]
        self.application_id = params["application_id"]
        self.guild_id = params["guild_id"]
        self.session_id = params["session_id"]
        self.authorization = params["authorization"]
        self.version = params["version"]
        self.id = params["id"]

        self.flags = flags

    def send(self, prompt) -> None:
        header = {"authorization": self.authorization}

        prompt = prompt.replace("_", " ")
        prompt = " ".join(prompt.split())
        prompt = re.sub(r"[^a-zA-Z0-9\s]+", "", prompt).lower()

        payload = {
            "type": 2,
            "application_id": self.application_id,
            "guild_id": self.guild_id,
            "channel_id": self.channel_id,
            "session_id": self.session_id,
            "data": {
                "version": self.version,
                "id": self.id,
                "name": "imagine",
                "type": 1,
                "options": [
                    {
                        "type": 3,
                        "name": "prompt",
                        "value": str(prompt) + " " + self.flags,
                    }
                ],
                "attachments": [],
            },
        }

        r = requests.post(url, json=payload, headers=header)

        while r.status_code != 204:
            logging.warning(f"Unable to send prompt. Trying again...")

            r = requests.post(
                "https://discord.com/api/v9/interactions", json=payload, headers=header
            )

        logging.info(f'Prompt "{prompt}" successfully sent.')
