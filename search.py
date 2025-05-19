import logging

from webex_bot.formatting import quote_info
from webex_bot.models.command import Command

log = logging.getLogger(__name__)


class SearchCommand(Command):

    def __init__(self):
        super().__init__(
            command_keyword="search",
            help_message="Search among the bot's knowledge base")

    def pre_execute(self, message: str, attachment_actions: dict, activity: dict):
        """
        (optional function).
        Reply before running the execute function.

        Useful to indicate the bot is handling it if it is a long running tsearch.

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """
        return quote_info(message)

    def execute(self, message: str, attachment_actions: dict, activity: dict) -> str:
        """
        If you want to respond to a submit operation on the card, you
        would write code here!

        You can return text string here or even another card (Response).

        This sample command function simply echos back the sent message.

        :param message: message with command already stripped
        :param attachment_actions: attachment_actions object
        :param activity: activity object

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """

        resp = ("Template response... This is where you would put your search results I guess.\n" +
                "I hope you like that answer! Try re-phrasing if you aren't satisfied.")
        return resp

# Callbacks are useful when using adaptive cards.
# class SearchCallback(Command):
#
#     def __init__(self):
#         super().__init__(
#             card_callback_keyword="search_callback"
#         )
#d
#     def execute(self, message: str, attachment_actions: dict, activity: dict) -> str:
        # resp = "Template response... This is where you would put your search results I guess.\n"
        # resp_closure = "I hope you like that answer! Try re-phrasing if you aren't satisfied."
        # return resp + resp_closure
