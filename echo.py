import logging

from webexpythonsdk.models.cards import TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Text
from webexpythonsdk.models.cards.actions import Submit

from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

from utils import default_loading_card

log = logging.getLogger(__name__)


class EchoCommand(Command):

    def __init__(self):
        super().__init__(
            command_keyword="echo",
            help_message="Echo Words Back to You!",
            chained_commands=[EchoCallback()])

    def pre_execute(self, message, attachment_actions, activity):
        """
        (optional function).
        Reply before running the execute function.

        Useful to indicate the bot is handling it if it is a long running tsearch.

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """
        return default_loading_card()

    def execute(self, message, attachment_actions, activity):
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

        text1 = TextBlock("Echo", weight=FontWeight.BOLDER, size=FontSize.MEDIUM)
        text2 = TextBlock("Type in something here and it will be echo'd back to you. How useful is that!",
                          wrap=True, isSubtle=True)
        input_text = Text(id="message_typed", placeholder="Type something here", maxLength=30)
        input_column = Column(items=[input_text], width=2)

        submit = Submit(title="Submit",
                        data={
                            "callback_keyword": "echo_callback"})

        card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=[text1, text2], width=2)]),
                  ColumnSet(columns=[input_column]),
                  ], actions=[submit])

        return response_from_adaptive_card(card)


class EchoCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="echo_callback",
            delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return quote_info(attachment_actions.inputs.get("message_typed"))