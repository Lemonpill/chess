COLORS = WHITE, BLACK = 1, -1
PIECES = PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = range(1, 7)
WP, WN, WB, WR, WQ, WK = WHITES = [WHITE * p for p in PIECES]
BP, BN, BB, BR, BQ, BK = BLACKS = [BLACK * p for p in PIECES]
FEN_MAP = {"P": WP, "N": WN, "B": WB, "R": WR, "Q": WQ, "K": WK, "p": BP, "n": BN, "b": BB, "r": BR, "q": BQ, "k": BK}
T, TR, R, BR, B, BL, L, TL = 8, 9, 1, -7, -8, -9, -1, 7
EMPTY = 0


def fen_color(s: str) -> int:
    return WHITE if s == "w" else BLACK


def fen_piece(s: str) -> list[int]:
    if s.isdigit():
        return [EMPTY] * int(s)
    else:
        return [FEN_MAP[s]]


def fen_board(s: str) -> list[int]:
    b = []
    pts = s.split("/")
    for p in reversed(pts):
        for s in p:
            b += fen_piece(s)
    return b


def fen_state(s: str):
    parts = s.split()
    board = fen_board(parts[0])
    color = fen_color(parts[1])
    return board, color


fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
state = fen_state(fen)
print(state)
