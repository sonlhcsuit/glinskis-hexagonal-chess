from config import PIECES


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
