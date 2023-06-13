import time, logging

from midjourney import Sender, Receiver
from midjourney.config import load_json_config


params = load_json_config()

# Read more about flags at https://docs.midjourney.com/docs/models
flags = "--v 5.1"

sender = Sender(params=params, flags=flags)
receiver = Receiver(params=params, local_path="generated_img")

prompt = "A long-heared man reading book sitting on the chair staying at center of the night street"


def get_image_from_midjourney(prompt):
    url = None

    while receiver.check_result_with_prompt(prompt) != True:
        time.sleep(5)
    while url == None:
        url = receiver.get_result_with_prompt(prompt)
    return url


def main():
    logging.basicConfig(level=logging.INFO)

    while True:
        prompt = input("Enter prompt: ")
        sender.send(prompt)

        com = input("Enter command: ")

        match com:
            case "get-url":
                try:
                    sender.send(prompt)

                    await message.bot.send_chat_action(
                        message.chat.id, types.ChatActions.UPLOAD_PHOTO
                    )

                    func = lambda: get_image_from_midjourney(prompt)
                    loop = asyncio.get_running_loop()
                    url = await loop.run_in_executor(None, func)

                    logging.info(
                        "Generated image URL has been retrieved. URL is " + url
                    )

                except Exception as e:
                    logging.error(
                        "Unfortunately, <b>Midjourney</b> needed for the task has been confused :("
                    )

                    raise e
            case "try-download":
                receiver.collecting_results()
                receiver.outputer()
                receiver.downloading_results()


if __name__ == "__main__":
    main()
