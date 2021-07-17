import numpy as np
from utils import neighbor
from config import impact, pattern


class Piece:
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6
    WHITE = 8
    BLACK = 16
    IMPACT = impact

    KNIGHT_PATTERN = pattern["KNIGHT"]
    BISHOP_PATTERN = pattern["BISHOP"]
    ROOK_PATTERN = pattern["ROOK"]

    def __init__(self, value, slot):
        """
        Create a piece on the board
        :param value: indicate the type of piece (pawn, knight,...)
        :param slot: location of itself on the board, value in the range from [1,70]
        """
        self.slot = slot
        if value > 16:
            self.value = value - 16
            self.team = Piece.BLACK
        else:
            self.value = value - 8
            self.team = Piece.WHITE

    def strategic_value(self):
        if self.team == Piece.BLACK:
            return -1 * Piece.IMPACT[self.value - 1]
        return Piece.IMPACT[self.value - 1]

    def __str__(self):
        piece_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
        return f"{piece_names[self.value - 1]} at {self.slot} with {self.strategic_value()}"

    @staticmethod
    def get_neighbors_of(slot):
        return neighbor(slot)

    @staticmethod
    def is_legal_slot(slot: int, state: np.ndarray, is_white: bool):
        """
        Validation the selected slot are available for is_white team next move to the slot
        White cannot conquer already occupied slot by its team (vice versa_
        :param slot: the selected slot, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: the team, true for white team and false for black team
        :return:
        """
        if slot == 0:
            return False
        if state[slot - 1] == 0:
            # empty slot
            return True
        if is_white:
            # must be black piece
            return state[slot - 1] > 16
        else:
            # must be white piece
            return 8 < state[slot - 1] < 16

    @staticmethod
    def get_next_moves_of(slot: int, state: np.ndarray) -> tuple:
        """
        Generate available moves for the piece of the board base on state
        :param slot: slot of the board, must be in range [1,70]
        :param state: state of the game, or the board
        :return:
        """
        if len(state) != 70 or slot > 70 or slot < 1:
            assert (False, "State of the game is not valid")

        piece_value = state[slot - 1]
        white = True
        moves = ()

        if piece_value > 16:
            piece_value = piece_value - 16
            white = False
        else:
            piece_value = piece_value - 8
        if piece_value == 1:
            # pawn
            moves = Piece.pawn_move(slot, state, white)
        elif piece_value == 2:
            # knight
            moves = Piece.knight_move(slot, state, white)
        elif piece_value == 3:
            # bishop
            moves = Piece.bishop_move(slot, state, white)
        elif piece_value == 4:
            # rook
            moves = Piece.rook_move(slot, state, white)
        elif piece_value == 5:
            # queen
            moves = Piece.queen_move(slot, state, white)
        elif piece_value == 6:
            # king
            moves = Piece.king_move(slot, state, white)
        return moves

    @staticmethod
    def pawn_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        """
        Generate next pawn piece moves currently located in slot
        :param slot: the slot which pawn piece located in, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: is_white: the team, true for white team and false for black team
        :return: the tuple contains next moves of pawn at slot
        """
        moves = []
        neighbors = Piece.get_neighbors_of(slot)
        if is_white:
            top = neighbors[0]
            top_left = neighbors[1]
            top_right = neighbors[5]
            if state[top - 1] == 0:
                moves.append(top)
            if state[top_left - 1] - 16 > 0:
                moves.append(top_left)
            if state[top_right - 1] - 16 > 0:
                moves.append(top_right)
        else:
            bottom = neighbors[3]
            bottom_left = neighbors[4]
            bottom_right = neighbors[2]
            if state[bottom - 1] == 0:
                moves.append(bottom)
            if 8 < state[bottom_left - 1] < 16:
                moves.append(bottom_left)
            if 8 < state[bottom_right - 1] < 16:
                moves.append(bottom_right)
        return tuple(moves)

    @staticmethod
    def knight_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        """
        Generate next knight piece moves currently located in slot
        :param slot: the slot which knight piece located in, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: is_white: the team, true for white team and false for black team
        :return: the tuple contains next moves of knight at slot
        """
        moves = []
        neighbors = Piece.get_neighbors_of(slot)
        for i in range(6):
            if neighbors[i] != 0:
                n = Piece.get_neighbors_of(neighbors[i])[i]
                if n != 0:
                    offset = Piece.get_neighbors_of(n)
                    move_1 = offset[Piece.KNIGHT_PATTERN[i][0]]
                    move_2 = offset[Piece.KNIGHT_PATTERN[i][1]]
                    if Piece.is_legal_slot(move_1, state, is_white):
                        moves.append(move_1)
                    if Piece.is_legal_slot(move_2, state, is_white):
                        moves.append(move_2)
        return tuple(moves)

    @staticmethod
    def bishop_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        """
        Generate next bishop piece moves currently located in slot
        :param slot: the slot which bishop piece located in, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: is_white: the team, true for white team and false for black team
        :return: the tuple contains next moves of bishop at slot
        """
        moves = []
        for direction in Piece.BISHOP_PATTERN:
            temp_slot = slot
            while True:
                neighbors = Piece.get_neighbors_of(temp_slot)
                if neighbors[direction[0]] != 0:
                    move = Piece.get_neighbors_of(neighbors[direction[0]])[direction[1]]
                    if Piece.is_legal_slot(move, state, is_white):
                        moves.append(move)
                        temp_slot = move
                        if state[move - 1] != 0:
                            break
                    else:
                        break
                else:
                    break
        return tuple(moves)

    @staticmethod
    def rook_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        """
        Generate next rook piece moves currently located in slot
        :param slot: the slot which rook piece located in, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: is_white: the team, true for white team and false for black team
        :return: the tuple contains next moves of rook at slot
        """
        moves = []
        for direction in Piece.ROOK_PATTERN:
            temp_slot = slot
            while True:
                neighbors = Piece.get_neighbors_of(temp_slot)
                move = neighbors[direction]
                if Piece.is_legal_slot(move, state, is_white):
                    moves.append(move)
                    temp_slot = move
                    if state[move - 1] != 0:
                        break
                else:
                    break
        return tuple(moves)

    @staticmethod
    def queen_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        """
        Generate next queen piece moves currently located in slot
        :param slot: the slot which queen piece located in, value must be in range [1,70]
        :param state: the board - state of the game, must be 70 integer element with index in the range [0,69]
        :param is_white: is_white: the team, true for white team and false for black team
        :return: the tuple contains next moves of queen at slot
        """
        return Piece.bishop_move(slot, state, is_white) + Piece.rook_move(slot, state, is_white)

    @staticmethod
    def king_move(slot: int, state: np.ndarray, is_white: bool) -> tuple:
        moves = []
        neighbors = Piece.get_neighbors_of(slot)
        for neighbor_slot in neighbors:
            if Piece.is_legal_slot(neighbor_slot, state, is_white):
                moves.append(neighbor_slot)
        return tuple(moves)
