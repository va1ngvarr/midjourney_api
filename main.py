import logging

from bot import start_bot
from config import TOKEN


"""
Enable logging at root program scope
with info-level of the importance
"""
logging.basicConfig(level=logging.INFO)


def main() -> None:
    # Start aiogram long-polling
    start_bot(TOKEN)


if __name__ == "__main__":
    main()
