from typing import TypedDict


DIMENSION = 8

NONE = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

BLACK = -1
WHITE = 1

W_P = WHITE * PAWN
W_N = WHITE * KNIGHT
W_B = WHITE * BISHOP
W_R = WHITE * ROOK
W_Q = WHITE * QUEEN
W_K = WHITE * KING

B_P = BLACK * PAWN
B_N = BLACK * KNIGHT
B_B = BLACK * BISHOP
B_R = BLACK * ROOK
B_Q = BLACK * QUEEN
B_K = BLACK * KING

N_DIR = (-1, 0)
NE_DIR = (-1, 1)
E_DIR = (0, 1)
SE_DIR = (1, 1)
S_DIR = (1, 0)
SW_DIR = (1, -1)
W_DIR = (0, -1)
NW_DIR = (-1, -1)

INITIAL_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FEN_MAP = {"P": W_P, "N": W_N, "B": W_B, "R": W_R, "Q": W_Q, "K": W_K, "p": B_P, "n": B_N, "b": B_B, "r": B_R, "q": B_Q, "k": B_K}


class CastRight(TypedDict):
    K: bool
    k: bool
    Q: bool
    q: bool


class GameState(TypedDict):
    color: int
    board: list[list[int]]
    eppos: tuple[int, int]
    cstlr: CastRight
    halfm: int
    fullm: int


class Move(TypedDict):
    src: tuple[int, int]
    tgt: tuple[int, int]
    cpt: tuple[int, int] | None


def alg_to_pos(square: str) -> tuple[int, int]:
    file = ord(square[0]) - ord("a")
    rank = int(square[1])
    row = DIMENSION - rank
    return row, file


def fen_state(fen: str) -> GameState:
    board_p, color_p, cstlr_p, eppos_p, halfm_p, fullm_p = fen.strip().split()
    board: list[list[int]] = []
    for f_row in board_p.split("/"):
        b_row: list[int] = []
        for c in f_row:
            if c.isdigit():
                b_row.extend([NONE] * int(c))
            else:
                b_row.append(FEN_MAP[c])
        board.append(b_row)
    color = WHITE if color_p == "w" else BLACK
    cstlr = {"K": "K" in cstlr_p, "Q": "Q" in cstlr_p, "k": "k" in cstlr_p, "q": "q" in cstlr_p}
    eppos = None if eppos_p == "-" else alg_to_pos(eppos_p)
    halfm, fullm = int(halfm_p), int(fullm_p)
    return GameState(color=color, board=board, eppos=eppos, cstlr=cstlr, halfm=halfm, fullm=fullm)


def is_color(p: int, color: int):
    if not p:
        return False
    return p * color > 0


def add_tups(t1: tuple[int, int], t2: tuple[int, int]):
    return t1[0] + t2[0], t1[1] + t2[1]


def coordinates_by_color(color: int, board: list[list[int]]):
    l: list[tuple[int, int]] = []
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            p = board[r][c]
            if not is_color(p, color):
                continue
            l.append((r, c))
    return l


def piece_type(board: list[list[int]], pos: tuple[int, int]):
    return abs(board[pos[0]][pos[1]])


def exists(pos: tuple[int, int]):
    rng = range(DIMENSION)
    return pos[0] in rng and pos[1] in rng


def pawn_steps(color: int, board: list[list[int]], pos: tuple[int, int]):
    l = []
    rnk_map = {BLACK: 1, WHITE: 7}
    dir_map = {BLACK: S_DIR, WHITE: N_DIR}
    first_m = pos[0] == rnk_map[color]
    dir_off = dir_map[color]
    j_times = 2 if first_m else 1
    nxt_pos = add_tups(pos, dir_off)
    while exists(nxt_pos) and j_times:
        next_p = board[nxt_pos[0]][nxt_pos[1]]
        if next_p:
            break
        l.append(Move(src=pos, tgt=nxt_pos, cap=None))
        nxt_pos = add_tups(nxt_pos, dir_off)
        j_times -= 1
    return l


def pawn_captures(color: int, board: list[list[int]], pos: tuple[int, int], eppos: tuple[int, int] | None):
    l = []
    stp_dir_map = {BLACK: S_DIR, WHITE: N_DIR}
    cap_dir_map = {BLACK: [SE_DIR, SW_DIR], WHITE: [NE_DIR, NW_DIR]}
    for cap_off in cap_dir_map[color]:
        nxt_pos = add_tups(pos, cap_off)
        if not exists(nxt_pos):
            continue
        p = board[nxt_pos[0]][nxt_pos[1]]
        if not is_color(p=p, color=color):
            l.append(Move(src=pos, tgt=nxt_pos, cap=nxt_pos))
        elif nxt_pos == eppos:
            stp_off = stp_dir_map[color]
            cap_pos = add_tups(nxt_pos, stp_off)
            l.append(Move(src=pos, tgt=eppos, cap=cap_pos))
        else:
            continue
    return l


def pawn_moves(color: int, board: list[list[int]], pos: tuple[int, int], eppos: tuple[int, int] | None):
    l = []
    l += pawn_steps(color=color, board=board, pos=pos)
    l += pawn_captures(color=color, board=board, pos=pos, eppos=eppos)
    return l


def knight_moves(color: int, board: list[list[int]], pos: tuple[int, int], **kwargs):
    l = []
    return l


def bishop_moves(color: int, board: list[list[int]], pos: tuple[int, int], **kwargs):
    l = []
    return l


def rook_moves(color: int, board: list[list[int]], pos: tuple[int, int], **kwargs):
    l = []
    return l


def queen_moves(color: int, board: list[list[int]], pos: tuple[int, int], **kwargs):
    l = []
    return l


def king_moves(color: int, board: list[list[int]], pos: tuple[int, int], **kwargs):
    l = []
    return l


def valid_moves(color: int, board: list[list[int]], eppos: tuple[int, int] | None):
    l = []
    func_map = {
        PAWN: pawn_moves,
        KNIGHT: knight_moves,
        BISHOP: bishop_moves,
        ROOK: rook_moves,
        QUEEN: queen_moves,
        KING: king_moves,
    }
    coordinates = coordinates_by_color(color, board)
    for pos in coordinates:
        t = piece_type(board=board, pos=pos)
        if t not in func_map:
            continue
        func = func_map[t]
        l += func(color=color, board=board, pos=pos, eppos=eppos)
    return l


state = fen_state(INITIAL_FEN)
print(state)
moves = valid_moves(
    color=state["color"],
    board=state["board"],
    eppos=state["eppos"],
)
print(moves)
