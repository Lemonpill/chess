from fen import fen_state
from engine import scan_moves
from ui import draw_state

"""
[0] board
[1] active color
[2] castling rights
[3] en passant square
[4] halfmove clock
[5] fullmove number
"""

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
state = fen_state(fen)
draw_state(state)
moves = scan_moves(state)
print(moves)
