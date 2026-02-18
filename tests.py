from move import encode_move
from move import decode_move


def test_encode_move_reg():
    src_bef = 0
    tgt_bef = 63
    cap_bef = 0
    vic_bef = 0
    mov_enc = encode_move(src_bef, tgt_bef)
    src_aft, tgt_aft, cap_aft, vic_aft = decode_move(mov_enc)
    assert src_aft == src_bef
    assert tgt_aft == tgt_bef
    assert cap_aft == cap_bef
    assert vic_aft == vic_bef


def test_encode_move_cap():
    src_bef = 0
    tgt_bef = 63
    cap_bef = 8
    vic_bef = 1
    mov_enc = encode_move(src_bef, tgt_bef, cap_bef, vic_bef)
    src_aft, tgt_aft, cap_aft, vic_aft = decode_move(mov_enc)
    assert src_aft == src_bef
    assert tgt_aft == tgt_bef
    assert cap_aft == cap_bef
    assert vic_aft == vic_bef


if __name__ == "__main__":
    test_encode_move_reg()
    test_encode_move_cap()
