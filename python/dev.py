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
            result[0] += off[0]
            result[1] += off[1]
            result[2] += off[2]
            result[3] += off[3]
            result[4] += off[4]
            result[5] += off[5]
            if board_number == 40:
                result[0] = 0
                result[1] = 0
                result[5] = 0
            elif board_number == 31:
                result[2] = 0
                result[3] = 0
                result[4] = 0
            elif board_number == key_values[i] and board_number < 31:
                result[3] = 0
                result[4] = 0
            elif board_number == key_values[i] and board_number > 31:
                result[3] = 0
                result[4] = 0
            elif board_number == key_values[i - 1] - 1 and board_number < 40:
                result[0] = 0
                result[5] = 0
            elif board_number == key_values[i - 1] - 1 and board_number > 40:
                result[0] = 0
                result[1] = 0
            for i in range(len(result)):
                result[i] = result[i] if 0 <= result[i] <= 70 else 0
            break



    return result


for i in range(1, 71):
    print(f"{i} {neighbor(i)}")
