from chessBoard import *
SIMPLE = 'SIMPLE'
COMPLEX = 'COMPLEX'
board = ChessBoard()

def position_evaluation(state):
    totalVal=0;
    for team in state:
        for kind in state[team]:
            for piece in state[team][kind]:
                totalVal+=piece.get_value()
    return totalVal;

def generate_black_moves(env,evaluationFunc=position_evaluation):
    moves = env.get_actions_of(BLACK)
    chose=[]
    for move in moves:
        new_state = env.new_state_from_move(move)
        eval = position_evaluation(new_state)
        chose.append((move,eval))
    print(chose)
    maxeval =min(chose,key=lambda x:x[1])
    return maxeval

# test=generate_black_moves(board)
def play(env,movegenerateFunc=generate_black_moves):
    while env.is_done() is None:
        # env.render()
        wmove = input('ENTER valid move of white:')
        print("WHITE MOVE:{}".format(wmove))
        env.perform_move(wmove)
        # env.render()
        bmove= movegenerateFunc(env)
        print("BLACK MOVE:{}".format(bmove))
        env.perform_move(bmove[0])
        select= input('WANNA RENDER?\n1.YES\n2.NO')
        if(select=='1'):
            env.render()
        # env.render()

play(board)
# print(test)
['d4 d5',' e5 d5','c3->c4']