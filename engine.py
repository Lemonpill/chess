from typing import List
from const import Move
from const import Square
from const import State
from const import Piece
from const import PieceType
from const import Color
from const import Board
from const import DIMENSION
from const import WHITE
from const import N
from const import NE
from const import SE
from const import S
from const import SW
from const import NW
from const import PAWN
from const import RANK_2
from const import RANK_7


def piece_type(piece: Piece) -> PieceType:
    return abs(piece)


def is_first_pawn_rank(pos: Square, color: Color) -> bool:
    rank = RANK_2 if color == WHITE else RANK_7
    return pos in rank


def file_of(pos: Square) -> int:
    return pos % DIMENSION


def move_on_board(move: Move) -> bool:
    src, tgt = move
    if not (0 <= tgt < 64):
        return False
    f_del = file_of(tgt) - file_of(src)
    return abs(f_del) <= 1


def is_enemy(color: Color, piece: Piece) -> bool:
    return color * piece < 0


def pawn_jumps(board: Board, color: Color, pos: Square) -> List[Move]:
    moves: List[Move] = []
    rem = 2 if is_first_pawn_rank(pos, color) else 1
    dta = N if color == WHITE else S
    src = pos
    nxt = 1
    while nxt <= rem:
        tgt = src + dta * nxt
        mov = (src, tgt)
        if not move_on_board(mov):
            break
        p = board[tgt]
        if p:
            break
        moves.append(mov)
        nxt += 1
    return moves


def pawn_captures(board: Board, color: Color, pos: Square) -> List[Move]:
    moves: List[Move] = []
    directions = [NE, NW] if color == WHITE else [SE, SW]
    src = pos
    for dir in directions:
        tgt = src + dir
        mov = (src, tgt)
        if not move_on_board(mov):
            continue
        p = board[tgt]
        if not is_enemy(color, p):
            continue
        moves.append(mov)
        src += 1
    return moves


def pawn_moves(state: State, pos: Square) -> List[Move]:
    board, color = state
    moves: List[Move] = []
    moves.extend(pawn_jumps(board, color, pos))
    moves.extend(pawn_captures(board, color, pos))
    return moves


def scan_moves(state: State):
    board, color = state
    moves: list[Move] = []
    for i, p in enumerate(board):
        if not p or p * color < 0:
            continue
        if piece_type(p) == PAWN:
            moves += pawn_moves(state, i)
    return moves
