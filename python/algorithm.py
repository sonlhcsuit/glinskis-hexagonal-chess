import numpy as np

from Board import Board
from Piece import Piece
from utils import default_notation
import time

# search algorithms
# board is

global selected_move


def minimax(board: Board, depth=3, is_white=True):
    global selected_move

    if depth == 0 or board.is_terminate():
        return board.evaluation()
    if is_white:
        value = -10000000000
        next_moves = board.next_moves(True)
        for next_move in next_moves:
            temp_v = minimax(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])), depth - 1,
                             False)
            if temp_v > value:
                value = temp_v
                selected_move = next_move
        return value
    else:
        # black player is minimizing player
        value = 10000000000
        next_moves = board.next_moves(False)
        for next_move in next_moves:
            temp_v = minimax(Board.from_notation(board.notation_after_move(next_move[0], next_move[1])), depth - 1,
                             True)
            if temp_v < value:
                value = temp_v
                selected_move = next_move
        return value


def time_running(func):
    t0 = time.process_time()
    print(f"Start time: {t0:.10f}")
    func()
    # print(selected_move)
    t1 = time.process_time()
    print(f"Finish time: {t1:.10f}")
    print(f"Elapse time: {t1 - t0:.10f}")
    print("------------------------------------------------------------------------------------------")


def minimax_test():
    board = Board.from_notation(default_notation)
    value = minimax(board)
    print(value)
    print(selected_move)
    # moves = list(board.next_moves(True))
    # for move in moves:
    #     print(Board.from_notation(board.notation_after_move(move[0], move[1])).evaluation())


time_running(minimax_test)

##minimax
# def max_search(env, TEAM, evaluationFunc=material_evaluation):
#     chose = []
#     game_result = env.is_done()
#
#     if (game_result is None):
#         if (TEAM == BLACK):
#             moves = env.get_actions_of(BLACK)
#         elif TEAM == WHITE:
#             moves = env.get_actions_of(WHITE)
#         ##### compute material value of childs board
#         for move in moves:
#             new_state = env.new_state_from_move(move)
#             value = evaluationFunc(new_state)
#             chose.append((move, value))
#
#         ##### if team is BLACK , getting the move which will make lowest material value of board , or the highest one (for WHITE)
#         if (TEAM == BLACK):
#             mineval = min(chose, key=lambda x: x[1])
#             return mineval
#         elif TEAM == WHITE:
#             maxeval = max(chose, key=lambda x: x[1])
#             return maxeval
#     return game_result


# def minimax(env, depth, team, evaluationFunc=material_evaluation):  # black get min -> white get max
#     if (env.is_done() is not None or depth == 0):
#         a = env.get_state()
#         value = evaluationFunc(a)
#         return None, value
#     if team == BLACK:  # min player
#         moves = env.get_actions_of(BLACK)
#         value = 10000000000
#         choice = None
#         for move in moves:
#             state = env.get_state(SIMPLE)  # get board
#             new_env = ChessBoard(state)  # new board like old board
#             new_env.perform_move(move)  # new board after do move
#             _, newValue = minimax(new_env, depth - 1, WHITE)
#             if (newValue < value):
#                 value = newValue
#                 choice = move
#         return choice, value
#     elif team == WHITE:  # max player
#         moves = env.get_actions_of(WHITE)
#         value = -10000000000
#         choice = None
#         for move in moves:
#             state = env.get_state(SIMPLE)
#             new_env = ChessBoard(state)
#             new_env.perform_move(move)
#             _, newValue = minimax(new_env, depth - 1, BLACK)
#             if (newValue > value):
#                 value = newValue
#                 choice = move
#         return choice, value


# def minimaxAlphaBeta(env, depth, alpha, beta, team,
#                      evaluationFunc=material_evaluation):  # black get min -> white get max alpha for white beta for black
#     if (env.is_done() is not None or depth == 0):
#         a = env.get_state()
#         value = evaluationFunc(a)
#         return None, value
#     if team == BLACK:  # min player
#         moves = env.get_actions_of(BLACK)
#         value = 10000000000
#         choice = None
#         for move in moves:
#             state = env.get_state(SIMPLE)  # get board
#             new_env = ChessBoard(state)  # new board like old board
#             new_env.perform_move(move)  # new board after do move
#             _, newValue = minimaxAlphaBeta(new_env, depth - 1, alpha, beta, WHITE)
#             # min
#             if (newValue < value):
#                 value = newValue
#                 choice = move
#             if (value < beta):
#                 beta = value
#             if (beta <= alpha):
#                 break
#         return choice, value
#     elif team == WHITE:  # max player
#         moves = env.get_actions_of(WHITE)
#         value = -10000000000
#         choice = None
#         for move in moves:
#             state = env.get_state(SIMPLE)
#             new_env = ChessBoard(state)
#             new_env.perform_move(move)
#             _, newValue = minimaxAlphaBeta(new_env, depth - 1, alpha, beta, BLACK)
#             # max
#             if (newValue > value):
#                 value = newValue
#                 choice = move
#             if (value > alpha):
#                 alpha = value
#             if alpha >= beta:
#                 break
#         return choice, value


# def OLD(env, depth, team, evaluationFunc=material_evaluation):  # black get min -> white get max
#     if (env.is_done() is not None or depth == 0):
#         a = env.get_state()
#         return evaluationFunc(a)
#     if team == BLACK:  # min player
#         moves = env.get_actions_of(BLACK)
#         chose = []
#         for move in moves:
#             state = env.get_state(SIMPLE)  # get board
#             new_env = ChessBoard(state)  # new board like old board
#             new_env.perform_move(move)  # new board after do move
#             value = OLD(new_env, depth - 1, WHITE)
#             chose.append((move, value))
#         minvalue = min(chose, key=lambda x: x[1])
#         return minvalue
#     elif team == WHITE:  # max player
#         moves = env.get_actions_of(WHITE)
#         chose = []
#         for move in moves:
#             state = env.get_state(SIMPLE)
#             new_env = ChessBoard(state)
#             new_env.perform_move(move)
#             value = OLD(new_env, depth - 1, BLACK)
#             chose.append((move, value))
#         maxvalue = max(chose, key=lambda x: x[1])
#         return maxvalue


# def negamax(env, depth, color, evaluationFunc=material_evaluation):
#     if (env.is_done() is not None or depth == 0):
#         a = env.get_state()
#         value = evaluationFunc(a)
#         return None, color * value
#     value = -100000000000000000
#     moves = None
#     if color == -1:
#         moves = env.get_actions_of(BLACK)
#     elif color == 1:
#         moves = env.get_actions_of(WHITE)
#     choice = None
#     for move in moves:
#         state = env.get_state(SIMPLE)  # get board
#         new_env = ChessBoard(state)  # new board like old board
#         new_env.perform_move(move)  # new board after do move
#         _, newValue = negamax(new_env, depth - 1, -1 * color)
#         newValue = - newValue
#         if (newValue > value):
#             value = newValue
#             choice = move
#     return choice, value


# def negamaxAlphaBeta(env, depth, alpha, beta, color, evaluationFunc=material_evaluation):
#     if (env.is_done() is not None or depth == 0):
#         a = env.get_state()
#         value = evaluationFunc(a)
#         return None, color * value
#     value = -100000000000000000
#     moves = None
#     if color == -1:
#         moves = env.get_actions_of(BLACK)
#     elif color == 1:
#         moves = env.get_actions_of(WHITE)
#     choice = None
#     for move in moves:
#         state = env.get_state(SIMPLE)  # get board
#         new_env = ChessBoard(state)  # new board like old board
#         new_env.perform_move(move)  # new board after do move
#         _, newValue = negamaxAlphaBeta(new_env, depth - 1, -beta, -alpha, -1 * color)
#         newValue = - newValue
#         if (newValue > alpha):
#             alpha = newValue
#         if (newValue > value):
#             value = newValue
#             choice = move
#         if alpha > beta:
#             break
#     return choice, value


######################################testing#################################
import time
# t0= time.process_time()
# print("# of actions: {}".format(len(board.get_actions_of(BLACK))))
# print(minimax(board,2,BLACK,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Minimax with depth=2: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(minimaxAlphaBeta(board,2,-10000000000,1000000000,BLACK,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Minimax and Alpha-Beta pruning with depth=2: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(minimax(board,3,BLACK,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Minimax with depth=3: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(minimaxAlphaBeta(board,3,-10000000000,1000000000,BLACK,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Minimax and Alpha-Beta pruning with depth=3: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(negamax(board,2,-1,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Negamax with depth=2: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(negamaxAlphaBeta(board,2,-10000000000,1000000000,-1,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Negamax and Alpha-Beta pruning with depth=2: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(negamax(board,3,-1,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Negamax with depth=3: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")
# t0= time.process_time()
# print(negamaxAlphaBeta(board,3,-10000000000,1000000000,-1,material_evaluation_with_coefficient))
# t1 = time.process_time() - t0
# print("Time elapsed Negamax and Alpha-Beta pruning with depth=3: {0:.10f}".format(t1))
# print("------------------------------------------------------------------------------------------")

# def tocsv(input):
#     f = open("test.csv", "w")
#     for i in input:
#         f.write("{},".format(i))
#     f.write("\n")
#     print('\n', end="")
#     for i in range(0, 10):
#         for j in input:
#             if (len(input[j]) - 1 < i):
#                 f.write("x,")
#             else:
#                 f.write("{},".format(input[j][i]))
#         f.write("\n")
#
# tocsv(king_pos)
