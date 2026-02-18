from typing import List
from const import Move
from const import Square
from const import State
from const import Piece
from const import PieceType
from const import Color
from const import Board
from const import Offset
from const import DIMENSION
from const import WHITE
from const import BLACK
from const import T
from const import TR
from const import R
from const import BR
from const import B
from const import BL
from const import L
from const import TL
from const import PAWN
from const import KNIGHT
from const import BISHOP
from const import ROOK
from const import QUEEN
from const import KING
from const import RANK_2
from const import RANK_7


def piece_type(piece: Piece) -> PieceType:
    return abs(piece)


def is_first_pawn_rank(pos: Square, color: Color) -> bool:
    rank = RANK_2 if color == WHITE else RANK_7
    return pos in rank


def file_of(pos: Square) -> int:
    return pos % DIMENSION


def is_valid_step(src: Square, tgt: Square) -> bool:
    if not (0 <= tgt < 64):
        return False
    f_del = file_of(tgt) - file_of(src)
    return abs(f_del) <= 1


def pawn_jumps(board: Board, color: Color, pos: Square) -> List[Move]:
    moves: List[Move] = []
    jmp_num = 2 if is_first_pawn_rank(pos, color) else 1
    jmp_del = T if color == WHITE else B
    jmp_src = pos
    jmp_tgt = jmp_src + jmp_del
    while jmp_num and is_valid_step(jmp_src, jmp_tgt):
        tgt_p = board[jmp_tgt]
        if tgt_p:
            break
        moves.append((pos, jmp_tgt))
        jmp_src += jmp_del
        jmp_num -= 1
    return moves


def pawn_captures(board: Board, color: Color, pos: Square) -> List[Move]:
    moves: List[Move] = []
    directions: List[Offset] = [TR, TL] if color == WHITE else [BR, BL]
    src = pos
    for dir in directions:
        tgt = src + dir
        if not is_valid_step(src, tgt):
            continue
        src += 1

    return moves


def pawn_moves(state: State, pos: Square) -> List[Move]:
    board, color = state
    moves: List[Move] = []
    moves.extend(pawn_jumps(board, color, pos))
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
