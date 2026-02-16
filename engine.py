import string
from typing import TypeAlias, List
from constants import *

T, TR, R, BR, B, BL, L, TL = 8, 9, 1, -7, -8, -9, -1, 7
FEN_PIECE = {"P": WP, "N": WN, "B": WB, "R": WR, "Q": WQ, "K": WK, "p": BP, "n": BN, "b": BB, "r": BR, "q": BQ, "k": BK}
GUI_PIECE = {BK: "♔", WK: "♚", BQ: "♕", WQ: "♛", BR: "♖", WR: "♜", BB: "♗", WB: "♝", BN: "♘", WN: "♞", BP: "♙", WP: "♟"}
GUI_BLANK = {1: "◻", -1: "◼"}


Color: TypeAlias = int
WHITE: Color = 1
BLACK: Color = -1
COLORS: List[Color] = [WHITE, BLACK]

Square: TypeAlias = int
A1, B1, C1, D1, E1, F1, G1, H1 = map(Square, range(8))
A2, B2, C2, D2, E2, F2, G2, H2 = map(Square, range(8, 16))
A3, B3, C3, D3, E3, F3, G3, H3 = map(Square, range(16, 24))
A4, B4, C4, D4, E4, F4, G4, H4 = map(Square, range(24, 32))
A5, B5, C5, D5, E5, F5, G5, H5 = map(Square, range(32, 40))
A6, B6, C6, D6, E6, F6, G6, H6 = map(Square, range(40, 48))
A7, B7, C7, D7, E7, F7, G7, H7 = map(Square, range(48, 56))
A8, B8, C8, D8, E8, F8, G8, H8 = map(Square, range(56, 64))
SQUARES: List[Square] = list[range(64)]


Move = tuple[
    Square,  # source
    Square,  # target
]

State = tuple[
    list[int],  # board
    int,  # color
]


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


def draw_state(state: State) -> None:
    board, color = state
    h = [string.ascii_lowercase[i].upper() for i in range(DIMENSION)]
    h.insert(0, " ")
    print(" ".join(h))
    i = 0
    for r in range(DIMENSION):
        r_lst = []
        for c in range(DIMENSION):
            if not r_lst:
                r_lst.append(str(r + 1))
            p = board[i]
            if p:
                p_s = GUI_PIECE[p]
            else:
                s_sym = 1 if (r + c) % 2 else -1
                p_s = GUI_BLANK[s_sym]
            r_lst.append(p_s)
            i += 1
        print(" ".join(r_lst))


def pawn_moves(state: State, pos: int) -> list[Move]:
    board, color = state
    first_rank = range(8, 16) if color == WHITE else range(48, 56)
    step_num = 2 if pos in first_rank else 1
    step_dir = T if color == WHITE else B
    moves: list[Move] = []
    step_src = pos
    step_tgt = step_src + step_dir
    while step_num and step_tgt in range(64):
        tgt_p = board[step_tgt]
        if tgt_p:
            break
        moves.append((pos, step_tgt))
        step_src += step_dir
        step_num -= 1
    return moves


def scan_moves(state: State):
    board, color = state
    moves: list[Move] = []
    for i, p in enumerate(board):
        if not p or p * color < 0:
            continue
        if abs(p) == PAWN:
            moves += pawn_moves(state, i)
    return moves
