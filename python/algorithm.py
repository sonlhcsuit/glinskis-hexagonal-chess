import numpy as np

from Board import Board
from Piece import Piece
from utils import default_notation
import time


# search algorithms
# board is
def minimax(board: Board, depth=3, is_white=True):
    if depth == 0 or board.is_terminate():
        return board.evaluation(), []

    if is_white:
        # white player is maximizing player

        value = -10000000000
        next_moves = board.next_moves(True)
        move = None

        for next_move in next_moves:
            temp_value, _ = minimax(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])),
                                    depth - 1, False)
            if temp_value > value:
                value = temp_value
                move = next_move
        return value, move
    else:
        # black player is minimizing player
        value = 10000000000
        next_moves = board.next_moves(False)
        move = None

        for next_move in next_moves:
            temp_value, _ = minimax(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])),
                                    depth - 1, True)
            if temp_value < value:
                value = temp_value
                move = next_move
        return value, move


def minimax_prunning(board: Board, alpha, beta, depth=3, is_white=True):
    if depth == 0 or board.is_terminate():
        return board.evaluation(), []

    if is_white:
        # white player is maximizing player

        value = -10000000000
        next_moves = board.next_moves(True)
        move = None

        for next_move in next_moves:
            temp_value, _ = minimax_prunning(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])), alpha,
                                    beta, depth - 1, False)
            if temp_value > value:
                value = temp_value
                move = next_move
            if value >= beta:
                break
            alpha = max(alpha,value)
        return value, move
    else:
        # black player is minimizing player
        value = 10000000000
        next_moves = board.next_moves(False)
        move = None

        for next_move in next_moves:
            temp_value, _ = minimax_prunning(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])), alpha,
                                    beta, depth - 1, True)
            if temp_value < value:
                value = temp_value
                move = next_move
            if value <= alpha:
                break
            beta = min(beta,value)
        return value, move


def time_running(func):
    t0 = time.process_time()
    print(f"Start time: {t0:.10f}")
    func()

    t1 = time.process_time()
    print(f"Finish time: {t1:.10f}")
    print(f"Elapse time: {t1 - t0:.10f}")
    print("------------------------------------------------------------------------------------------")


def minimax_test():
    board = Board.from_notation(default_notation)
    value = minimax_prunning(board,-10000000,100000000)
    print(value)

# time_running(minimax_test)

