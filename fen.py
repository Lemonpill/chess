from const import State
from const import NONE
from const import WHITE
from const import BLACK
from const import WP
from const import BP
from const import WN
from const import BN
from const import WB
from const import BB
from const import WR
from const import BR
from const import WQ
from const import BQ
from const import WK
from const import BK


FEN_PIECE = {
    "P": WP,
    "N": WN,
    "B": WB,
    "R": WR,
    "Q": WQ,
    "K": WK,
    "p": BP,
    "n": BN,
    "b": BB,
    "r": BR,
    "q": BQ,
    "k": BK,
}


def fen_color(s: str) -> int:
    return WHITE if s == "w" else BLACK


def fen_piece(s: str) -> list[int]:
    if s.isdigit():
        return [NONE] * int(s)
    else:
        return [FEN_PIECE[s]]


def fen_board(s: str) -> list[int]:
    b = []
    pts = s.split("/")
    for p in reversed(pts):
        for s in p:
            b += fen_piece(s)
    return b


def fen_state(s: str) -> State:
    parts = s.split()
    board = fen_board(parts[0])
    color = fen_color(parts[1])
    return board, color
