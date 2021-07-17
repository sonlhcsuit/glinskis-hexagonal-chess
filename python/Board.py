from Piece import *
from utils import encode_notation, decode_notation



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

    return coef * pureVal * coefTable[position[0]][int(position[1:]) - 1]


class Board:
    def __init__(self, state: tuple):
        self.state: np.ndarray = np.array(state)

    def move(self, from_slot, to_slot):
        state: np.ndarray = self.state.copy()
        state[to_slot] = state[from_slot]
        state[from_slot] = 0
        return

    def notation_after_move(self, from_slot, to_slot):
        state: np.ndarray = self.state.copy()
        state[to_slot] = state[from_slot]
        state[from_slot] = 0
        return Board.encode(state)

    def state_after_move(self, from_slot, to_slot) -> np.ndarray:
        state: np.ndarray = self.state.copy()
        state[to_slot] = state[from_slot]
        state[from_slot] = 0
        return state

    def evaluation(self):

        return 0


    @staticmethod
    def encode(state: np.ndarray) -> str:
        return encode_notation(tuple(state))

    @staticmethod
    def decode(notation: str) -> np.ndarray:
        return np.array(decode_notation(notation))

    @staticmethod
    def from_notation(notation: str):
        return Board(tuple(Board.decode(notation)))

    @staticmethod
    def from_state(state: np.ndarray):
        return Board(tuple(state))
