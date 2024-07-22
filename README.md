# ygo-deck-stats

Jupyter Notebook for calculating how bricky your deck is

## Deck.txt format

Deck.txt schema:

```text
CARDS # This field is required, after this go the cards
<card name> <count of cards> <type of card> <deck type>

# i.e.
snake_eye_ash 3 m (for monster) e (for engine)

COMBOS # This field indicates to start defining combos
<weight> <card 1> <optional card 2> <optional card 3>

# i.e.
6 snake_eye_ash

# 2 card
5 snake_eye_ash diabellstar_the_black_witch
```

Possible values for `card_type` (3rd card field)(see [deck.py](models/deck.py#L4)):

- `m`: monster
- `s`: spell
- `t`: trap

Possible values for `deck_card_type` (4th card field)(see [deck.py](models/deck.py#L10)):

- `e`: engine
- `ne`: non-engine
- `b`: brick
