def isValidChessBoard(board):
    white_king = 0
    black_king = 0
    black_pieces = 0
    white_pieces = 0
    black_pawns = 0
    white_pawns = 0
    isSquare = True

    for piece in board.values():
        if piece == 'bK':
            black_king += 1
        elif piece == 'wK':
            white_king += 1

        if piece[0] == 'w':
            white_pieces += 1
        elif piece[0] == 'b':
            black_pieces += 1

        if piece[0] == 'w' and piece[1] == 'P':
            white_pawns += 1
        elif piece[0] == 'b' and piece[1] == 'P':
            black_pawns += 1

    for square in board.keys():
        if square[0] not in 'abcdefgh' or square[1] not in '12345678':
            isSquare = False

    if (white_king == 1 and black_king == 1 and white_pieces <= 16 and
        black_pieces <= 16 and white_pawns <= 8 and black_pawns <= 8 and
        isSquare == True):
        return True
    else:
        return False


board = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
print(isValidChessBoard(board))