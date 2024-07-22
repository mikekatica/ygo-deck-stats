import pytest
import unittest
from unittest.mock import patch, mock_open
from models import deck


@pytest.fixture(scope="class")
def get_file_content(request):
    file_txt = """
CARDS
snake_eye_ash 3 m e
snake_eye_poplar 2 m e
snake_eyes_diabellstar 1 m b
COMBOS
1 snake_eye_poplar
2 snake_eye_ash
"""
    request.cls.content = file_txt

_CARDS = [
        deck.Card(
            "snake_eye_ash",
            3,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
        ),
        deck.Card(
            "snake_eye_poplar",
            2,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
        ),
        deck.Card(
            "snake_eyes_diabellstar",
            1,
            deck.CardType.MONSTER,
            deck.DeckCardType.BRICK
        ),
    ]

_COMBOS = [
        deck.Combo([_CARDS[0]], 2),
        deck.Combo(_CARDS[1:2], 1)
    ]

@pytest.mark.parametrize("card", _CARDS)
def test_card_str_repr(card):
    name = card.name
    assert str(card) == name
    assert card.__repr__() == name


@pytest.mark.usefixtures("get_file_content")
class ParserTest(unittest.TestCase):

    def test_parser(self):
        with patch("builtins.open", mock_open(read_data=self.content)) as mock_file:
            d = deck.Deck.from_file("my_file_name")
            mock_file.assert_called_once_with("my_file_name", "r")
        assert d.__class__ == deck.Deck
        cards = d.cards
        assert len(cards) == 3
        assert deck.Card(
            "snake_eye_ash",
            3,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
        ) in cards
        assert deck.Card(
            "snake_eye_poplar",
            2,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
        ) in cards
        assert deck.Card(
            "snake_eyes_diabellstar",
            1,
            deck.CardType.MONSTER,
            deck.DeckCardType.BRICK
        ) in cards
        c1 = deck.Combo([
            deck.Card(
            "snake_eye_ash",
            3,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
            )],
            2
        )
        c2 = deck.Combo([
            deck.Card(
            "snake_eye_poplar",
            2,
            deck.CardType.MONSTER,
            deck.DeckCardType.ENGINE
            )],
            1
        )
        assert c1 in d.combos
        assert c2 in d.combos