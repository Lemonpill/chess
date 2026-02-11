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

BOARD = [
    [W_R, W_N, W_B, W_Q, W_K, W_B, W_N, W_R],
    [W_P] * 8,
    [NONE] * 8,
    [NONE] * 8,
    [NONE] * 8,
    [NONE] * 8,
    [B_P] * 8,
    [B_R, B_N, B_B, B_Q, B_K, B_B, B_N, B_R],
]


def is_color(p: int, color: int):
    return p * color > 0


def is_enemy(p: int, color: int):
    if not color:
        return False
    return p * color < 0


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
    cur_r, cur_c = pos
    rnk_map = {WHITE: 1, BLACK: 7}
    dir_map = {WHITE: S_DIR, BLACK: N_DIR}
    first_m = cur_r == rnk_map[color]
    dir_r, dir_c = dir_map[color]
    j_times = 2 if first_m else 1
    nxt_r = cur_r + dir_r
    nxt_c = cur_c + dir_c
    nxt_pos = (nxt_r, nxt_c)
    while exists(nxt_pos) and j_times:
        next_p = board[nxt_r][nxt_c]
        if next_p:
            break
        l.append((pos, nxt_pos, None))
        nxt_r += dir_r
        nxt_c += dir_c
        j_times -= 1
    return l


def pawn_captures(color: int, board: list[list[int]], pos: tuple[int, int], enp_pos: tuple[int, int] | None):
    l = []
    stp_dir_map = {WHITE: S_DIR, BLACK: N_DIR}
    cap_dir_map = {WHITE: [SE_DIR, SW_DIR], BLACK: [NE_DIR, NW_DIR]}
    cur_r, cur_c = pos
    for dir_r, dir_c in cap_dir_map[color]:
        nxt_r = cur_r + dir_r
        nxt_c = cur_c + dir_c
        nxt_pos = (nxt_r, nxt_c)
        if not exists(nxt_pos):
            continue
        p = board[nxt_r][nxt_c]
        if is_enemy(p=p, color=color):
            l.append((pos, nxt_pos, nxt_pos))
        elif nxt_pos == enp_pos:
            cap_pos = nxt_r + stp_dir_map[color], nxt_c
            l.append((pos, enp_pos, cap_pos))
        else:
            continue
    return l


def pawn_moves(color: int, board: list[list[int]], pos: tuple[int, int], enp_pos: tuple[int, int] | None):
    l = []
    l += pawn_steps(color=color, board=board, pos=pos)
    l += pawn_captures(color=color, board=board, pos=pos, enp_pos=enp_pos)
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


def valid_moves(color: int, board: list[list[int]], enp_pos: tuple[int, int] | None):
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
        l += func(color=color, board=board, pos=pos, enp_pos=enp_pos)
    return l


color = WHITE
enp_pos = None
moves = valid_moves(color=color, board=BOARD, enp_pos=enp_pos)
print(moves)
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
