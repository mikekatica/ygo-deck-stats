import pytest
import unittest
from unittest.mock import patch, mock_open
from models import deck


@pytest.fixture(scope="class")
def get_file_content(request):
    file_txt = """
CARDS
bonfire 3 s e
snake_eye_ash 3 m e
snake_eye_poplar 2 m e
COMBOS
1 snake_eye_poplar
1 bonfire
2 snake_eye_ash
"""
    request.cls.content = file_txt


@pytest.mark.usefixtures("get_file_content")
class ParserTest(unittest.TestCase):

    def test_parser(self):
        with patch("builtins.open", mock_open(read_data=self.content)) as mock_file:
            d = deck.Deck.from_file("my_file_name")
            assert d.__class__ == deck.Deck
            mock_file.assert_called_once_with("my_file_name", "r")
            cards = d.cards
            assert len(cards) == 3
            assert deck.Card(
                "snake_eye_ash",
                3,
                deck.CardType.MONSTER,
                deck.DeckCardType.ENGINE
            ) in cards