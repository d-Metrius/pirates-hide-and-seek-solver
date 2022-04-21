WHITE_SHIP = 'W'
RED_SHIP = 'R'
ISLAND = 'I'
CAVE = 'C'
BOAT = 'B'

MAX_WHITE_SHIPS = 5
MAX_RED_SHIPS = 3
MAX_ISLANDS = 3
MAX_CAVES = 2
MAX_BOATS = 3

MAX_OBJECTS = 7
MIN_OBJECTS = 3

DATA1 = [
    [BOAT, None, BOAT],
    [None, None, None],
    [WHITE_SHIP, None, CAVE],
]

DATA2 = [
    [None, None, CAVE],
    [None, RED_SHIP, None],
    [ISLAND, None, WHITE_SHIP],
]

DATA3 = [
    [RED_SHIP, None, WHITE_SHIP],
    [None, ISLAND, None],
    [None, None, WHITE_SHIP],
]

DATA4 = [
    [BOAT, None, RED_SHIP],
    [None, WHITE_SHIP, None],
    [None, None, ISLAND],
]

DATA = [
    DATA1,
    DATA2,
    DATA3,
    DATA4,
]

MASK1 = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
]

MASK2 = [
    [1, 1, 1],
    [1, 1, 1],
    [0, 1, 1],
]

MASK3 = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 1],
]

MASK4 = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
]
