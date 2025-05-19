import json
import os
import sys

from dotenv import load_dotenv
from webex_bot.commands.help import HelpCommand
from webex_bot.webex_bot import WebexBot

from search import SearchCommand
from echo import EchoCommand


def main():
    load_dotenv()

    # Proxy configuration
    # Supports https or wss proxy, wss prioritized.
    proxies = None
    # Create a Bot Object
    bot = WebexBot(teams_bot_token=os.getenv("BOT_TOKEN"),
        approved_users=json.loads(os.getenv('APPROVED_USER_IDS')),
        approved_rooms=json.loads(os.getenv('APPROVED_ROOM_IDS')),
        bot_name="Hello World Bot",
        include_demo_commands=True,
        proxies=proxies)

    # Add new commands for the bot to listen out for.
    bot.add_command(EchoCommand())
    bot.add_command(SearchCommand())

    # Call `run` for the bot to wait for incoming messages.
    bot.run()


if __name__ == '__main__':
    main()
