from enum import Enum
from typing import List

class CardType(Enum):
    MONSTER = "m"
    SPELL = "s"
    TRAP = "t"


class DeckCardType(Enum):
    BRICK = "b"
    ENGINE = "e"
    NONENGINE = "ne"


class _ReadMode(Enum):
    NONE = "NONE"
    CARDS = "CARDS"
    COMBOS = "COMBOS"


class Card():
    def __init__(self, name: str, count: int, type: CardType, deck_type: DeckCardType) -> None:
        self.name = name
        self.count = count
        self.type = type
        self.deck_type = deck_type
    
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class Combo():
    def __init__(self, cards: List[Card], weight: int) -> None:
        self.cards = cards
        self.weight = weight

    def __str__(self) -> str:
        card_names = [
            i.name
            for i in self.cards
        ]
        return " + ".join(card_names)
    
    def __repr__(self) -> str:
        return self.__str__()


class Deck():
    def __init__(self, initial_cards: List[Card], initial_combos: List[Combo]) -> None:
        self.cards = initial_cards
        self.combos = initial_combos
        self._calculate_size()
    
    def _calculate_size(self):
        self.size = sum([
            i.count
            for i in self.cards
        ])

    def add_card(self, card: Card):
        self.cards.append(card)
        self._calculate_size()

    def add_combo(self, combo: Combo):
        self.combos.append(combo)

    def card_by_name(self, name: str):
        card = list(filter(
            lambda x: x.name == name,
            self.cards
        ))
        if len(card) > 1:
            raise ValueError(f"Too many cards match \"{name}\"")
        else:
            return card[0]
    
    def cards_by_deck_type(self, type: DeckCardType):
        cards = list(filter(
            lambda x: x.deck_type == type,
            self.cards
        ))
        return cards
    
    def get_simulated_cards(self):
        out = []
        for card in self.cards:
            out.extend([
                card for _ in range(0,card.count)
            ])
        return out

    
    def __str__(self) -> str:
        return "\n".join([
            f"{i.name}:{i.count}"
            for i in self.cards
        ])

    @classmethod
    def from_file(_, filepath: str):
        print(filepath)
        deck = Deck([], [])
        with open(filepath, "r") as f:
            mode = _ReadMode.NONE
            for line in f.readlines():
                sline = line.strip("\n")
                match sline:
                    case "CARDS":
                        mode = _ReadMode(sline)
                        continue
                    case "COMBOS":
                        mode = _ReadMode(sline)
                        continue
                    case _:
                        match mode:
                            case _ReadMode.CARDS:
                                card = sline.split(" ")
                                deck.add_card(Card(
                                    card[0],
                                    int(card[1]),
                                    CardType(card[2]),
                                    DeckCardType(card[3])
                                ))
                            case _ReadMode.COMBOS:
                                combo = sline.split(" ")
                                weight = int(combo[0])
                                cards_str = combo[1:]
                                cards = [
                                    deck.card_by_name(i)
                                    for i in cards_str
                                ]
                                deck.add_combo(Combo(
                                    cards, weight
                                ))
                            case _:
                                pass
        return deck
