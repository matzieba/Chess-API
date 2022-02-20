def moves_generator(index, chessboard, n):
    moves = []
    try:
        for i in range(1, n):
            move_right = chessboard[index[0]][index[1] + i]
            moves.append(move_right)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_right_down = chessboard[index[0] + i][index[1] + i]
            moves.append(move_right_down)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_right_up = chessboard[index[0] - i][index[1] + i]
            if (index[0] - i) < 0:
                pass
            else:
                moves.append(move_right_up)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_left_down = chessboard[index[0] + i][index[1] - i]
            if (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left_down)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_left_up = chessboard[index[0] - i][index[1] - i]
            if (index[0] - i) < 0:
                pass
            elif (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left_up)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_left = chessboard[index[0]][index[1] - i]
            if (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_up = chessboard[index[0] - i][index[1]]
            if (index[0] - i) < 0:
                pass
            else:
                moves.append(move_up)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_down = chessboard[index[0] + i][index[1]]
            moves.append(move_down)
    except IndexError:
        pass
    return moves


def moves_generator_rock(index, chessboard, n):
    moves = []
    try:
        for i in range(1, n):
            move_right = chessboard[index[0]][index[1] + i]
            moves.append(move_right)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_left = chessboard[index[0]][index[1] - i]
            if (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_up = chessboard[index[0] - i][index[1]]
            if (index[0] - i) < 0:
                pass
            else:
                moves.append(move_up)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_down = chessboard[index[0] + i][index[1]]
            moves.append(move_down)
    except IndexError:
        pass
    return moves


def moves_generator_bischop(index, chessboard, n):
    moves = []
    try:
        for i in range(1, n):
            move_right_down = chessboard[index[0] + i][index[1] + i]
            moves.append(move_right_down)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_right_up = chessboard[index[0] - i][index[1] + i]
            if (index[0] - i) < 0:
                pass
            else:
                moves.append(move_right_up)
    except IndexError:
        pass
    try:
        for i in range(1, n):
            move_left_down = chessboard[index[0] + i][index[1] - i]
            if (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left_down)
    except IndexError:
        pass

    try:
        for i in range(1, n):
            move_left_up = chessboard[index[0] - i][index[1] - i]
            if (index[0] - i) < 0:
                pass
            elif (index[1] - i) < 0:
                pass
            else:
                moves.append(move_left_up)
    except IndexError:
        pass
    return moves


def moves_generator_knight(index, chessboard):
    moves = []
    # right_up
    try:
        move = chessboard[index[0] - 1][index[1] + 2]
        if (index[0] - 1) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass

    try:
        move = chessboard[index[0] - 2][index[1] + 1]
        if (index[0] - 2) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass
    # left_up
    try:
        move = chessboard[index[0] - 1][index[1] - 2]
        if (index[0] - 1) < 0:
            pass
        elif (index[1] - 2) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass
    try:
        move = chessboard[index[0] - 2][index[1] - 1]
        if (index[0] - 2) < 0:
            pass
        elif (index[1] - 1) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass
    # right_down
    try:
        move = chessboard[index[0] + 1][index[1] + 2]
        moves.append(move)
    except IndexError:
        pass

    try:
        move = chessboard[index[0] + 2][index[1] + 1]
        moves.append(move)
    except IndexError:
        pass
    # left_down
    try:
        move = chessboard[index[0] + 1][index[1] - 2]
        if (index[1] - 2) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass

    try:
        move = chessboard[index[0] + 2][index[1] - 1]
        if (index[1] - 1) < 0:
            pass
        else:
            moves.append(move)
    except IndexError:
        pass
    return moves


def moves_generator_pawn(index, chessboard):
    moves = []
    try:
        move_up = chessboard[index[0] - 1][index[1]]
        if (index[0] - 1) < 0:
            pass
        else:
            moves.append(move_up)
    except IndexError:
        pass

    try:
        move_down = chessboard[index[0] + 1][index[1]]
        moves.append(move_down)
    except IndexError:
        pass
    return moves
