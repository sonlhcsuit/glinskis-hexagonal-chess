from flask import Flask,request,jsonify
from runtime import *
import json
app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    # print(request.get_json())
    return jsonify({"result":"WELCOME TO GLINSKI CHESS!"})

@app.route('/move',methods=['post'])
def response_move():
    state = request.get_json()
    # print(state)
    state = json.loads(state)
    temp_board = ChessBoard(state)
    result  = minimax(temp_board,1,BLACK)
    print(result)
    if(result == WHITE or result == BLACK):
        return {"game_state":result}
    return {"black_move":result[0]}

@app.route('/checkwin',methods=['post'])
def checkwin():
    state = request.get_json()
    state = json.loads(state)
    temp_board = ChessBoard(state)
    result = temp_board.is_done()
    if (result == WHITE or result == BLACK):
        print({"winner": result})
        return {"winner": result}
    else:
        print({"winner":"not yet"})
        return {"winner":"not yet"}
if __name__ == '__main__':
    app.run(debug=True)