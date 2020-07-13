from chessBoard import *
SIMPLE = 'SIMPLE'
COMPLEX = 'COMPLEX'
board = ChessBoard()

#evaluation function

def material_evaluation(state):
    totalVal=0
    for team in state:
        for kind in state[team]:
            for piece in state[team][kind]:
                totalVal+=piece.get_value()
    return totalVal



#search alogrithm

##minimax
def max_search(env,TEAM):
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
            value = material_evaluation(new_state)
            chose.append((move, value))

        ##### if team is BLACK , getting the move which will make lowest material value of board , or the highest one (for WHITE)
        if (TEAM == BLACK):
            mineval = min(chose, key=lambda x: x[1])
            return mineval
        elif TEAM == WHITE:
            maxeval = max(chose, key=lambda x: x[1])
            return maxeval
    return game_result
#
# def alphabeta(env,depth,team): # black get min -> white get max
#     if(env.is_done() is not None or depth==0):
#         a=env.get_state()
#         return material_evaluation(a)
#     if team == BLACK:#min player
#         moves = env.get_actions_of(BLACK)
#         minval = 1000000
#         for move in moves:
#             state = env.get_state(SIMPLE)# get board
#             new_env = ChessBoard(state) #new board like old board
#             new_env.perform_move(move) # new board after do move
#
#             value = alphabeta(new_env,depth-1,WHITE)
#             if value < minval:
#                 minval = value
#                 print(team,move,value)
#         print(team,"--------------------------------------")
#         return minval
#     elif team == WHITE:#max player
#         moves = env.get_actions_of(WHITE)
#         maxval=-100000
#         for move in moves:
#             state = env.get_state(SIMPLE)
#             new_env = ChessBoard(state)
#             new_env.perform_move(move)
#             value = alphabeta(new_env,depth-1,BLACK)
#             if value > maxval:
#                 maxval=value
#                 print(team,move,value)
#         print(team,"--------------------------------------")
#         return maxval

def minimax(env,depth,team): # black get min -> white get max
    if(env.is_done() is not None or depth==0):
        a=env.get_state()
        return material_evaluation(a)
    if team == BLACK:#min player
        moves = env.get_actions_of(BLACK)
        chose = []
        for move in moves:
            state = env.get_state(SIMPLE)# get board
            new_env = ChessBoard(state) #new board like old board
            new_env.perform_move(move) # new board after do move
            value = minimax(new_env,depth-1,WHITE)
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
            value = minimax(new_env,depth-1,BLACK)
            chose.append((move,value))
        maxvalue = max(chose, key=lambda x: x[1])
        return maxvalue
## play function
def generate_next_moves(env,team=BLACK,searchFunc=max_search):
    team = team.upper()
    if team == BLACK or team == WHITE:
        return searchFunc(env,team)
    else:
        return "INVALID TEAM"
# test=generate_black_moves(board)
# def play(env,movegenerateFunc=generate_black_moves):
#     while env.is_done() is None:
#         # env.render()
#         wmove = input('ENTER valid move of white:')
#         print("WHITE MOVE:{}".format(wmove))
#         env.perform_move(wmove)
#         # env.render()
#         bmove= movegenerateFunc(env)
#         print("BLACK MOVE:{}".format(bmove))
#         env.perform_move(bmove[0])
#         select= input('WANNA RENDER?\n1.YES\n2.NO')
#         if(select=='1'):
#             env.render()






######################################testing#################################
# print(board.is_done())
# print(material_evaluation(board.get_state()))
# board.render()
# print(board.get_actions_of(WHITE))
# move = max_search(board,WHITE)
# print(move)
# board.perform_move(move[0])
# print(board.get_actions_of(WHITE))
# move = max_search(board,WHITE)
# print(move)

# print(alphabeta(board,2,BLACK))
# print(select_move)
