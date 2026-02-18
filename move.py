from const import Square
from const import Piece


MSK_4 = 0b1111
MSK_6 = 0b111111

SRC_PAD = 0
TGT_PAD = 6
CAP_PAD = 12
VIC_PAD = 18


def encode_move(src: Square, tgt: Square, cap: Square = 0, vic: Piece = 0):
    return (src << SRC_PAD) | (tgt << TGT_PAD) | (cap << CAP_PAD) | (vic << VIC_PAD)


def decode_move(mov: int):
    src = (mov >> SRC_PAD) & MSK_6
    tgt = (mov >> TGT_PAD) & MSK_6
    cap = (mov >> CAP_PAD) & MSK_6
    vic = (mov >> VIC_PAD) & MSK_4
    return src, tgt, cap, vic
