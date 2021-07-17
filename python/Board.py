import numpy as np

from Piece import *
from utils import encode_notation, decode_notation, default_notation
from config import coefficient


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

    def evaluation(self, is_coefficient: bool = False):
        evaluation_value = 0
        if is_coefficient:
            indexes = np.where(self.state != 0)

            def strategic_value_with_coefficient(piece, slot):
                piece_value = piece - 16 if piece > 16 else piece - 8
                if piece_value == Piece.PAWN:
                    if piece > 16:
                        return Piece.strategic_value_of(piece) * coefficient["PAWN_BLACK"][slot]
                    else:
                        return Piece.strategic_value_of(piece) * coefficient["PAWN"][slot]

                elif piece_value == Piece.KNIGHT:
                    return Piece.strategic_value_of(piece) * coefficient["KNIGHT"][slot]
                elif piece_value == Piece.BISHOP:
                    return Piece.strategic_value_of(piece) * coefficient["BISHOP"][slot]

                elif piece_value == Piece.ROOK:
                    return Piece.strategic_value_of(piece) * coefficient["ROOK"][slot]

                elif piece_value == Piece.QUEEN:
                    return Piece.strategic_value_of(piece) * coefficient["QUEEN"][slot]

                elif piece_value == Piece.KING:
                    return Piece.strategic_value_of(piece) * coefficient["KING"][slot]

                return 0

            func = np.vectorize(strategic_value_with_coefficient)
            result = func(self.state[self.state != 0], indexes)
            evaluation_value = sum(result)
        else:
            strategic_value = np.vectorize(Piece.strategic_value_of)
            pieces: np.ndarray = self.state[self.state != 0]
            evaluation_value = sum(strategic_value(pieces))

        return evaluation_value

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


board = Board.from_notation(default_notation)
print(board.evaluation(True))
