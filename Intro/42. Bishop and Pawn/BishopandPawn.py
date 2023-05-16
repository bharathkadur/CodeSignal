def solution(bishop, pawn):
    bishop_row, bishop_col = ord(bishop[0]) - ord('a'), int(bishop[1])
    pawn_row, pawn_col = ord(pawn[0]) - ord('a'), int(pawn[1])
    return abs(bishop_row - pawn_row) == abs(bishop_col - pawn_col)
