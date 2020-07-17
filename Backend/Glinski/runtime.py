from chessBoard import *

SIMPLE = 'SIMPLE'
COMPLEX = 'COMPLEX'
board = ChessBoard()

# evaluation function
pawn_pos_white = {
    "A": [0, 1, 0.5, 0.75, -1, -2],
    "B": [0, 0, 0, 0.5, 0.75, -1, -2],
    "C": [0, 0, 0, 0, 0.5, 0.75, -1, -2],
    "D": [0, 0, 0, 0, 0, 0.5, 0.75, -1, -2],
    "E": [0, 0, 0, 0, 0, 0, 00.5, 0.75, -1, -2],
    "F": [0, 0, 0, 0, 0, 0.5, 0.75, -1, -2],
    "G": [0, 0, 0, 0, 0.5, 0.75, -1, -2],
    "H": [0, 0, 0, 0.5, 0.75, -1, -2],
    "I": [0, 1, 0.5, 0.75, -1, -2]
}
pawn_pos_black = {
    "A": [-2, -1, 0.75, 0.5, 1, 0],
    "B": [-2, -1, 0.75, 0.5, 0, 0, 0],
    "C": [-2, -1, 0.75, 0.5, 0, 0, 0, 0],
    "D": [-2, -1, 0.75, 0.5, 0, 0, 0, 0, 0],
    "E": [-2, -1, 0.75, 0.5, 0, 0, 0, 0, 0, 0],
    "F": [-2, -1, 0.75, 0.5, 0, 0, 0, 0, 0],
    "G": [-2, -1, 0.75, 0.5, 0, 0, 0, 0],
    "H": [-2, -1, 0.75, 0.5, 0, 0, 0],
    "I": [-2, -1, 0.75, 0.5, 1, 0]
}
bishop_pos = {
    "A": [-2, -1, -0.5, -0.5, -1, -2],
    "B": [-1, 0.5, 1, 0, 1, 0.5, -1],
    "C": [-0.5, 0, 1, 0, 2, 1, 0, -0.5],
    "D": [-1, -0.5, 1, 2, 2, 2, 1, -0.5, -1],
    "E": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "F": [-1, -0.5, 1, 2, 2, 2, 1, -0.5, -1],
    "G": [-0.5, 0, 1, 0, 2, 1, 0, -0.5],
    "H": [-1, 0.5, 1, 0, 1, 0.5, -1],
    "I": [-2, -1, -0.5, -0.5, -1, -2],
}
knight_pos = {
    "A": [-5, -4, -3, -3, -4, -5],
    "B": [-4, -3, -2, -1, -2, -3, -4],
    "C": [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
    "D": [-2, 0, 1, 1.5, 2, 1.5, 1, 0, -2],
    "E": [-1, 0.5, 1.5, 2, 2, 2, 2, 1.5, 0.5, -1],
    "F": [-2, 0, 1, 1.5, 2, 1.5, 1, 0, -2],
    "G": [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
    "H": [-4, -3, -2, -1, -2, -3, -4],
    "I": [-5, -4, -3, -3, -4, -5],
}
rook_pos = {
    "A": [-1, 1, 1, 1, 1, -1],
    "B": [0.5, 1, 1, 1, 1, 1, 0.5],
    "C": [0.5, 1, 1.5, 1.5, 1.5, 1.5, 1, 0.5],
    "D": [0.5, 1, 1.5, 2, 2, 2, 1.5, 1, 0.5],
    "E": [-1, 1.5, 2, 2, 2, 2, 2, 2, 1.5, -1],
    "F": [0.5, 1, 1.5, 2, 2, 2, 1.5, 1, 0.5],
    "G": [0.5, 1, 1.5, 1.5, 1.5, 1.5, 1, 0.5],
    "H": [0.5, 1, 1, 1, 1, 1, 0.5],
    "I": [-1, 1, 1, 1, 1, -1],
}
queen_pos = {
    "A": [-2, -1, 1, 1, -1, -2],
    "B": [-1, 0, 0, 0.5, 0, 0, -1],
    "C": [-0.5, 1, 1.5, 1.5, 1.5, 1.5, 1, 0.5],
    "D": [-1, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
    "E": [-2, -1, 0, 0.5, 1, 1, 1, 0.5, -1, -2],
    "F": [-1, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
    "G": [-0.5, 1, 1.5, 1.5, 1.5, 1.5, 1, 0.5],
    "H": [-1, 0, 0, 0.5, 0, 0, -1],
    "I": [-2, -1, 1, 1, -1, -2],
}
king_pos = {
    "A": [-2, -1, 1, 1, -1, -2],
    "B": [-1, 0.5, 1, 1, 1, 0.5, -1],
    "C": [0.5, 1, 1, 1, 1, 1, 1, 0.5],
    "D": [-1, 1, 1, 2, 2, 2, 1, 1, -1],
    "E": [-2, 1, 1, 2, 2, 2, 2, 1, 1, -2],
    "F": [-1, 1, 1, 2, 2, 2, 1, 1, -1],
    "G": [0.5, 1, 1, 1, 1, 1, 1, 0.5],
    "H": [-1, 0.5, 1, 1, 1, 0.5, -1],
    "I": [-2, -1, 1, 1, -1, -2],
}

def material_evaluation(state):
    totalVal = 0
    for team in state:
        for kind in state[team]:
            for piece in state[team][kind]:
                totalVal += piece.get_value()
    return totalVal


def coefficient_value(piece):
    coef = 1
    coefTable = None
    if (piece.get_team() == BLACK):
        coef = -1
    coefTable = None
    if (piece.get_type() == PAWN and piece.get_team() == BLACK):
        coefTable = pawn_pos_black
    elif (piece.get_type() == PAWN and piece.get_team() == WHITE):
        coefTable = pawn_pos_white
    elif (piece.get_type() == KNIGHT):
        coefTable = knight_pos
    elif (piece.get_type() == BISHOP):
        coefTable = bishop_pos
    elif (piece.get_type() == ROOK):
        coefTable = rook_pos
    elif (piece.get_type() == QUEEN):
        coefTable = queen_pos
    elif (piece.get_type() == KING):
        coefTable = king_pos
    pureVal = piece.get_value()
    position = piece.get_position()

    return coef*pureVal * coefTable[position[0]][int(position[1:])-1]

def material_evaluation_with_coefficient(state):
    totalVal = 0
    for team in state:
        for kind in state[team]:
            for piece in state[team][kind]:
                totalVal += coefficient_value(piece)
    return totalVal

# search alogrithm

##minimax
def max_search(env, TEAM,evaluationFunc=material_evaluation):
    chose = []
    game_result = env.is_done()

    if (game_result is None):
        if (TEAM == BLACK):
            moves = env.get_actions_of(BLACK)
        elif TEAM == WHITE:
            moves = env.get_actions_of(WHITE)
        ##### compute material value of childs board
        for move in moves:
            new_state = env.new_state_from_move(move)
            value = evaluationFunc(new_state)
            chose.append((move, value))

        ##### if team is BLACK , getting the move which will make lowest material value of board , or the highest one (for WHITE)
        if (TEAM == BLACK):
            mineval = min(chose, key=lambda x: x[1])
            return mineval
        elif TEAM == WHITE:
            maxeval = max(chose, key=lambda x: x[1])
            return maxeval
    return game_result

def minimax(env,depth,team,evaluationFunc=material_evaluation): # black get min -> white get max
    if(env.is_done() is not None or depth==0):
        a=env.get_state()
        value = evaluationFunc(a)
        return None,value
    if team == BLACK:#min player
        moves = env.get_actions_of(BLACK)
        value = 10000000000
        choice = None
        for move in moves:
            state = env.get_state(SIMPLE)# get board
            new_env = ChessBoard(state) #new board like old board
            new_env.perform_move(move) # new board after do move
            _,newValue = minimax(new_env,depth-1,WHITE)
            if(newValue < value):
                value=newValue
                choice = move
        return choice,value
    elif team == WHITE:#max player
        moves = env.get_actions_of(WHITE)
        value = -10000000000
        choice = None
        for move in moves:
            state = env.get_state(SIMPLE)
            new_env = ChessBoard(state)
            new_env.perform_move(move)
            _, newValue = minimax(new_env, depth - 1, BLACK)
            if (newValue > value):
                value = newValue
                choice = move
        return choice, value

def minimaxAlphaBeta(env,depth,alpha,beta,team,evaluationFunc=material_evaluation): # black get min -> white get max alpha for white beta for black
    if(env.is_done() is not None or depth==0):
        a=env.get_state()
        value = evaluationFunc(a)
        return None,value
    if team == BLACK:#min player
        moves = env.get_actions_of(BLACK)
        value = 10000000000
        choice = None
        for move in moves:
            state = env.get_state(SIMPLE)# get board
            new_env = ChessBoard(state) #new board like old board
            new_env.perform_move(move) # new board after do move
            _,newValue = minimaxAlphaBeta(new_env,depth-1,alpha,beta,WHITE)
            #min
            if(newValue < value):
                value=newValue
                choice = move
            if(value < beta):
                beta = value
            if(beta <= alpha):
                break
        return choice,value
    elif team == WHITE:#max player
        moves = env.get_actions_of(WHITE)
        value = -10000000000
        choice = None
        for move in moves:
            state = env.get_state(SIMPLE)
            new_env = ChessBoard(state)
            new_env.perform_move(move)
            _, newValue = minimaxAlphaBeta(new_env,depth - 1,alpha,beta, BLACK)
            #max
            if (newValue > value):
                value = newValue
                choice = move
            if (value > alpha):
                alpha = value
            if alpha>=beta:
                break
        return choice, value

def OLD(env,depth,team,evaluationFunc=material_evaluation): # black get min -> white get max
    if(env.is_done() is not None or depth==0):
        a=env.get_state()
        return evaluationFunc(a)
    if team == BLACK:#min player
        moves = env.get_actions_of(BLACK)
        chose = []
        for move in moves:
            state = env.get_state(SIMPLE)# get board
            new_env = ChessBoard(state) #new board like old board
            new_env.perform_move(move) # new board after do move
            value = OLD(new_env,depth-1,WHITE)
            chose.append((move,value))
        minvalue = min(chose, key=lambda x: x[1])
        return minvalue
    elif team == WHITE:#max player
        moves = env.get_actions_of(WHITE)
        chose = []
        for move in moves:
            state = env.get_state(SIMPLE)
            new_env = ChessBoard(state)
            new_env.perform_move(move)
            value = OLD(new_env,depth-1,BLACK)
            chose.append((move,value))
        maxvalue = max(chose, key=lambda x: x[1])
        return maxvalue

def negamax(env,depth,color,evaluationFunc=material_evaluation):
    if (env.is_done() is not None or depth == 0):
        a = env.get_state()
        value = evaluationFunc(a)
        return None, color*value
    value = -100000000000000000
    moves = None
    if color == -1:
        moves = env.get_actions_of(BLACK)
    elif color==1:
        moves = env.get_actions_of(WHITE)
    choice = None
    for move in moves:
        state = env.get_state(SIMPLE)  # get board
        new_env = ChessBoard(state)  # new board like old board
        new_env.perform_move(move)  # new board after do move
        _, newValue = negamax(new_env, depth - 1, -1*color)
        newValue = - newValue
        if (newValue > value):
            value = newValue
            choice = move
    return choice, value

def negamaxAlphaBeta(env,depth,alpha,beta,color,evaluationFunc=material_evaluation):
    if (env.is_done() is not None or depth == 0):
        a = env.get_state()
        value = evaluationFunc(a)
        return None, color*value
    value = -100000000000000000
    moves = None
    if color == -1:
        moves = env.get_actions_of(BLACK)
    elif color==1:
        moves = env.get_actions_of(WHITE)
    choice = None
    for move in moves:
        state = env.get_state(SIMPLE)  # get board
        new_env = ChessBoard(state)  # new board like old board
        new_env.perform_move(move)  # new board after do move
        _, newValue = negamaxAlphaBeta(new_env, depth - 1,-beta,-alpha, -1*color)
        newValue = - newValue
        if(newValue >alpha):
            alpha = newValue
        if (newValue > value):
            value = newValue
            choice = move
        if alpha>beta:
            break
    return choice, value
######################################testing#################################
# import time
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

def tocsv(input):
    f = open("test.csv", "w")
    for i in input:
        f.write("{},".format(i))
    f.write("\n")
    print('\n', end="")
    for i in range(0, 10):
        for j in input:
            if (len(input[j]) - 1 < i):
                f.write("x,")
            else:
                f.write("{},".format(input[j][i]))
        f.write("\n")

tocsv(king_pos)