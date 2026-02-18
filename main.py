from fen import fen_state
from engine import scan_moves
from ui import draw_state

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
state = fen_state(fen)
draw_state(state)
moves = scan_moves(state)
print(moves)
