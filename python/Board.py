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
        state[to_slot - 1] = state[from_slot - 1]
        state[from_slot - 1] = 0
        return Board.encode(state)

    def state_after_move(self, from_slot, to_slot) -> np.ndarray:
        state: np.ndarray = self.state.copy()
        state[to_slot - 1] = state[from_slot - 1]
        state[from_slot - 1] = 0
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
            result = func(self.state[self.state != 0], indexes[0])
            evaluation_value = sum(result)
        else:
            strategic_value = np.vectorize(Piece.strategic_value_of)
            pieces: np.ndarray = self.state[self.state != 0]
            evaluation_value = sum(strategic_value(pieces))

        return evaluation_value

    def next_moves(self, is_white: bool = True) -> np.ndarray:
        indexes = None
        if is_white:
            indexes = np.where(self != 0 and self.state < 16)
        else:
            indexes = np.where(self.state > 16)

        def next_move_of_piece(index):
            moves = Piece.get_next_moves_of(index + 1, self.state)
            v = np.array([[index + 1, m] for m in moves])
            return v.flatten()

        moves: np.ndarray = np.array([next_move_of_piece(index) for index in indexes[0]], dtype=object)
        moves: np.ndarray = np.concatenate(moves)
        moves: np.ndarray = np.reshape(moves, (-1, 2))
        return moves.astype(int)

    def is_terminate(self) -> bool:
        if self.state[self.state == 8 + 6].shape[0] == 0:
            return True
        if self.state[self.state == 16 + 6].shape[0] == 0:
            return True
        return False

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

