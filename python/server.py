from flask import Flask, request, jsonify
from algorithm import *
import json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    # print(request.get_json())
    return jsonify({"result": "WELCOME TO GLINSKI CHESS!"})


@app.route('/move', methods=['post'])
def response_move():
    state = request.get_json()
    print(state)
    state = json.loads(state)
    temp_board = ChessBoard(state['board'])
    team = state['team']
    print(state)
    result = None
    if team.upper() == BLACK:
        result = minimaxAlphaBeta(temp_board, 4, -10000000000, 1000000000, BLACK, material_evaluation_with_coefficient)
    else:
        result = minimaxAlphaBeta(temp_board, 4, -10000000000, 1000000000, WHITE, material_evaluation_with_coefficient)
    print(result)
    return {
        "team": team,
        "move": result[0]}


@app.route('/checkwin', methods=['post'])
def evaluate_winning_status():
    state = request.get_json()
    state = json.loads(state)
    temp_board = ChessBoard(state['board'])
    result = temp_board.is_done()
    if (result == WHITE or result == BLACK):
        print({"winner": result})
        return {"winner": result}
    else:
        print({"winner": "not yet"})
        return {"winner": "not yet"}


if __name__ == '__main__':
    app.run(debug=True)
