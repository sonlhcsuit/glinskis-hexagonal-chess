def neighbor(board_number: int) -> tuple:
    if not (0 < board_number < 71):
        raise Exception("Board number are not valid, must in the range [1,70]")
    result = [board_number for _ in range(6)]
    key_values = (65, 58, 50, 41, 31, 22, 14, 7, 1)
    offset = (
        (1, 6, 5, -1, -7, -6),
        (1, 7, 6, -1, -8, -7),
        (1, 8, 7, -1, -9, -8),
        (1, 9, 8, -1, -10, -9),
        (1, 10, 9, -1, -10, -9),  # mid
        (1, 10, 9, -1, -9, -8),
        (1, 9, 8, -1, -8, -7),
        (1, 8, 7, -1, -7, -6),
        (1, 7, 6, -1, -6, -5),
    )
    for i in range(len(key_values)):
        if board_number >= key_values[i]:
            off: tuple = offset[i]
            result = [result[i] + off[i] for i in range(len(result))]
            if board_number == 40:
                result[0] = result[1] = result[5] = 0
            elif board_number == 31:
                result[2] = result[3] = result[4] = 0
            elif board_number == key_values[i] and board_number < 31:
                result[3] = result[4] = 0
            elif board_number == key_values[i] and board_number > 31:
                result[2] = result[3] = 0
            elif board_number == key_values[i - 1] - 1 and board_number < 40:
                result[0] = result[5] = 0
            elif board_number == key_values[i - 1] - 1 and board_number > 40:
                result[0] = result[1] = 0
            for i in range(len(result)):
                result[i] = result[i] if 0 <= result[i] <= 70 else 0
            break
    return tuple(result)


# lower case is white & upper case is black
default_notation = "6_rp3_PRn1_p2_P1_Nq2_p1_P2_Qbbb1_pP1_BBBk2_p2_P1_Kn1_p3_PNrp3_PR"
default_board = tuple([
    0, 0, 0, 0, 0, 0,  # a
    12, 9, 0, 0, 0, 17, 20,  # b
    10, 0, 9, 0, 0, 17, 0, 18,  # c
    13, 0, 0, 9, 0, 17, 0, 0, 21,  # d
    11, 11, 11, 0, 9, 17, 0, 19, 19, 19,  # e
    14, 0, 0, 9, 0, 17, 0, 0, 22,  # f
    10, 0, 9, 0, 0, 17, 0, 18,  # g
    12, 9, 0, 0, 0, 17, 20,  # h
    0, 0, 0, 0, 0, 0,  # i
])

# pawn, knight , bishop rook queen king
PIECES = 'pnbrqk//PNBRQK//'
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6
WHITE = 8
BLACK = 16


def decode_notation(notation: str) -> tuple:
    board = [0 for _ in range(70)]
    current_index = 0
    empty_slot = ""

    for char in notation:
        if char.isdigit():
            empty_slot += char
        elif char == "_":
            num = int(empty_slot)
            current_index = current_index + num
            empty_slot = ""
        elif char in PIECES:
            board[current_index] = 8 + PIECES.index(char) + 1
            current_index += 1

    return tuple(board)


def encode_notation(board: tuple) -> str:
    if len(board) != 70:
        raise Exception("Board size is not valid")
    notation = ""
    empty_slot = 0
    for i in range(len(board)):
        slot = board[i]
        if slot == 0:
            empty_slot += 1
        else:
            if empty_slot != 0:
                notation = f"{notation}{empty_slot}_"
                empty_slot = 0
            notation = f"{notation}{PIECES[slot - 8 - 1]}"

    return notation

