from typing import TypeAlias
from typing import List

DIMENSION = 8

Color: TypeAlias = int
WHITE: Color = 1
BLACK: Color = -1
COLORS: List[Color] = [WHITE, BLACK]

Square: TypeAlias = int
A1: Square = 0
B1: Square = 1
C1: Square = 2
D1: Square = 3
E1: Square = 4
F1: Square = 5
G1: Square = 6
H1: Square = 7

A2: Square = 8
B2: Square = 9
C2: Square = 10
D2: Square = 11
E2: Square = 12
F2: Square = 13
G2: Square = 14
H2: Square = 15

A3: Square = 16
B3: Square = 17
C3: Square = 18
D3: Square = 19
E3: Square = 20
F3: Square = 21
G3: Square = 22
H3: Square = 23

A4: Square = 24
B4: Square = 25
C4: Square = 26
D4: Square = 27
E4: Square = 28
F4: Square = 29
G4: Square = 30
H4: Square = 31

A5: Square = 32
B5: Square = 33
C5: Square = 34
D5: Square = 35
E5: Square = 36
F5: Square = 37
G5: Square = 38
H5: Square = 39

A6: Square = 40
B6: Square = 41
C6: Square = 42
D6: Square = 43
E6: Square = 44
F6: Square = 45
G6: Square = 46
H6: Square = 47

A7: Square = 48
B7: Square = 49
C7: Square = 50
D7: Square = 51
E7: Square = 52
F7: Square = 53
G7: Square = 54
H7: Square = 55

A8: Square = 56
B8: Square = 57
C8: Square = 58
D8: Square = 59
E8: Square = 60
F8: Square = 61
G8: Square = 62
H8: Square = 63
SQUARES: List[Square] = list(range(64))

PieceType: TypeAlias = int
NONE: PieceType = 0
PAWN: PieceType = 1
KNIGHT: PieceType = 2
BISHOP: PieceType = 3
ROOK: PieceType = 4
QUEEN: PieceType = 5
KING: PieceType = 6
PIECE_TYPES: List[PieceType] = list(range(1, 7))

Piece: TypeAlias = int
WP: Piece = PAWN * WHITE
BP: Piece = PAWN * BLACK
WN: Piece = KNIGHT * WHITE
BN: Piece = KNIGHT * BLACK
WB: Piece = BISHOP * WHITE
BB: Piece = BISHOP * BLACK
WR: Piece = ROOK * WHITE
BR: Piece = ROOK * BLACK
WQ: Piece = QUEEN * WHITE
BQ: Piece = QUEEN * BLACK
WK: Piece = KING * WHITE
BK: Piece = KING * BLACK
