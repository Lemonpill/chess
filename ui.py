import string
from const import State
from const import DIMENSION
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


GUI_PIECE = {BK: "♔", WK: "♚", BQ: "♕", WQ: "♛", BR: "♖", WR: "♜", BB: "♗", WB: "♝", BN: "♘", WN: "♞", BP: "♙", WP: "♟"}
GUI_BLANK = {1: "◻", -1: "◼"}


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
