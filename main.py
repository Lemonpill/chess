from engine import *

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
state = fen_state(fen)
print(state)
draw_state(state)
moves = scan_moves(state)
print(moves)
