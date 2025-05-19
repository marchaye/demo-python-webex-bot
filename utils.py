from webex_bot.models.response import response_from_adaptive_card
from webexpythonsdk.models.cards import Image, TextBlock, HorizontalAlignment, Colors, FontWeight, ColumnSet, Column, \
    AdaptiveCard, FontSize


def default_loading_card():
    """
    :return: a string or Response object (or a list of either). Use Response if you want to return another card.
    """

    image = Image(url="https://i.postimg.cc/2jMv5kqt/AS89975.jpg")
    text1 = TextBlock("Working on it....", weight=FontWeight.BOLDER, wrap=True, size=FontSize.DEFAULT,
        horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
    text2 = TextBlock("I am busy working on your request. Please continue to look busy while I do your work.",
        horizontalAlignment=HorizontalAlignment.CENTER, wrap=True, color=Colors.DARK)
    card = AdaptiveCard(
        body=[ColumnSet(columns=[Column(items=[image], width=2)]),
              ColumnSet(columns=[Column(items=[text1, text2])]),
              ])

    return response_from_adaptive_card(card)
