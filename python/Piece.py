import numpy as np
from utils import neighbor


class Piece:
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6
    WHITE = 8
    BLACK = 16
    IMPACT = np.array([10, 30, 60, 100, 250, 900])

    KNIGHT_PATTERN = [
        [5, 1],
        [0, 2],
        [1, 3],
        [2, 4],
        [3, 5],
        [4, 0],
    ]

    BISHOP_PATTERN = [
        [0, 1],
        [0, 5],
        [2, 1],
        [2, 3],
        [4, 3],
        [4, 5]
    ]
    ROOK_PATTERN = [0, 1, 2, 3, 4, 5]

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
        return f"{piece_names[self.value - 1]} at {self.slot}"

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
            #	    	must be white piece
            return 8 < state[slot - 1] < 16

    @staticmethod
    def get_next_moves_of(slot: int, state: np.ndarray) -> tuple:
        """
        Generate available moves for the piece of the board base on state
        :param slot: slot of the board, must be in range [1,70]
        :param state: state of the game, or the boad
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

#
#
#
#     def __init__(self, value,slot):
#         self.position = position  # string
#         self.type = type  # string
#         self.team = team  # string
#         self.moveable = []
#         coefficent = 1 if team == WHITE else -1
#         if (type == PAWN):
#             self.value = coefficent * 10
#         elif type == KNIGHT:
#             self.value = coefficent * 30
#         elif type == BISHOP:
#             self.value = coefficent * 60
#         elif type == ROOK:
#             self.value = coefficent * 100
#         elif type == QUEEN:
#             self.value = coefficent * 250
#         elif type == KING:
#             self.value = coefficent * 900
#
#     def team(self):
#         return Pieces.BLACK if self.value > Pieces.BLACK else Pieces.WHITE
#
#     def value(self):
#         return self.value;
#
#     def valid_position(self, position):
#         if position[0] == 'A' or position[0] == 'I':
#             return int(position[1:]) <= 6 and int(position[1:]) >= 1
#         elif position[0] == 'B' or position[0] == 'H':
#             return int(position[1:]) <= 7 and int(position[1:]) >= 1
#         elif position[0] == 'C' or position[0] == 'G':
#             return int(position[1:]) <= 8 and int(position[1:]) >= 1
#         elif position[0] == 'D' or position[0] == 'F':
#             return int(position[1:]) <= 9 and int(position[1:]) >= 1
#         elif position[0] == 'E':
#             return int(position[1:]) <= 10 and int(position[1:]) >= 1
#         else:
#             return False
#
#     def get_position(self):
#         return self.position
#
#     def get_value(self):
#         return self.value
#
#     def get_team(self):
#         return self.team
#
#     def get_type(self):
#         return self.type
#
#     def get_moveable(self):
#         return self.moveable
#
#     def get_positon_around(self, current_pos):
#         if (current_pos == None):
#             return [None, None, None, None, None, None]
#         col = current_pos[0]
#         row = int(current_pos[1:])
#         arround_pos = []
#         if (col == 'E'):
#             down = '{}{}'.format(col, row - 1)
#             leftDown = '{}{}'.format(chr(ord(col) - 1), row - 1)
#             leftTop = '{}{}'.format(chr(ord(col) - 1), row)
#             top = '{}{}'.format(col, row + 1)
#             rightTop = '{}{}'.format(chr(ord(col) + 1), row)
#             rightDown = '{}{}'.format(chr(ord(col) + 1), row - 1)
#             arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
#             arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
#         if (col < 'E'):
#             down = '{}{}'.format(col, row - 1)
#             leftDown = '{}{}'.format(chr(ord(col) - 1), row - 1)
#             leftTop = '{}{}'.format(chr(ord(col) - 1), row)
#             top = '{}{}'.format(col, row + 1)
#             rightTop = '{}{}'.format(chr(ord(col) + 1), row + 1)
#             rightDown = '{}{}'.format(chr(ord(col) + 1), row)
#             arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
#             arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
#         if (col > 'E'):
#             down = '{}{}'.format(col, row - 1)
#             leftDown = '{}{}'.format(chr(ord(col) - 1), row)
#             leftTop = '{}{}'.format(chr(ord(col) - 1), row + 1)
#             top = '{}{}'.format(col, row + 1)
#             rightTop = '{}{}'.format(chr(ord(col) + 1), row)
#             rightDown = '{}{}'.format(chr(ord(col) + 1), row - 1)
#             arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
#             arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
#         return arround_pos
#
#     def get_down_position(self, position):
#         return self.get_positon_around(position)[0]
#
#     def get_leftDown_position(self, position):
#         return self.get_positon_around(position)[1]
#
#     def get_leftTop_position(self, position):
#         return self.get_positon_around(position)[2]
#
#     def get_top_position(self, position):
#         return self.get_positon_around(position)[3]
#
#     def get_rightTop_position(self, position):
#         return self.get_positon_around(position)[4]
#
#     def get_rightDown_position(self, position):
#         return self.get_positon_around(position)[5]
#
#     def generate_moves(self, position):
#         return position
#
#     def get_info(self):
#         return (self.team, self.type, self.position, self.value)
#
#     def __str__(self):
#         # return self.get_info()
#         return '{} {} {} {}'.format(self.team, self.type, self.position, self.value)
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Pawn(Pieces):
#     def __init__(self, team, position):
#         super(Pawn, self).__init__(team, PAWN, position)
#
#     def generate_pawn_moves(self, position):
#         if (self.team == WHITE):
#             lt = self.get_leftTop_position(position)
#             t = self.get_top_position(position)
#             rt = self.get_rightTop_position(position)
#             self.moveable = [[t], [lt, rt]]
#             return self.moveable
#         elif self.team == BLACK:
#             ld = self.get_leftDown_position(position)
#             d = self.get_down_position(position)
#             rd = self.get_rightDown_position(position)
#             self.moveable = [[d], [ld, rd]]
#             return self.moveable
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_pawn_moves(self.position)
#         else:
#             return self.generate_pawn_moves(position)
#
#
# class Knight(Pieces):
#     def __init__(self, team, position):
#         super(Knight, self).__init__(team, KNIGHT, position)
#
#     def generate_knight_moves(self, position):
#         move = []
#         # left bottom
#         tempPos = self.get_down_position(position)
#         tempPos = self.get_leftDown_position(tempPos)
#         move.append(self.get_down_position(tempPos))
#         move.append(self.get_leftDown_position(tempPos))
#         # right bottom
#         tempPos = self.get_down_position(position)
#         tempPos = self.get_rightDown_position(tempPos)
#         move.append(self.get_down_position(tempPos))
#         move.append(self.get_rightDown_position(tempPos))
#         # left middle
#         tempPos = self.get_leftDown_position(position)
#         tempPos = self.get_leftTop_position(tempPos)
#         move.append(self.get_leftDown_position(tempPos))
#         move.append(self.get_leftTop_position(tempPos))
#         # right middle
#         tempPos = self.get_rightDown_position(position)
#         tempPos = self.get_rightTop_position(tempPos)
#         move.append(self.get_rightDown_position(tempPos))
#         move.append(self.get_rightTop_position(tempPos))
#         # left top
#         tempPos = self.get_top_position(position)
#         tempPos = self.get_leftTop_position(tempPos)
#         move.append(self.get_leftTop_position(tempPos))
#         move.append(self.get_top_position(tempPos))
#         # right top
#         tempPos = self.get_top_position(position)
#         tempPos = self.get_rightTop_position(tempPos)
#         move.append(self.get_top_position(tempPos))
#         move.append(self.get_rightTop_position(tempPos))
#         return move
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_knight_moves(self.position)
#         else:
#             return self.generate_knight_moves(position)
#
#
# class Bishop(Pieces):
#     def __init__(self, team, position):
#         super(Bishop, self).__init__(team, BISHOP, position)
#
#     def bishop_bottom_left(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_down_position(temp)
#             temp = self.get_leftDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def bishop_bottom_right(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_down_position(temp)
#             temp = self.get_rightDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def bishop_middle_left(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_leftTop_position(temp)
#             temp = self.get_leftDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def bishop_middle_right(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_rightTop_position(temp)
#             temp = self.get_rightDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def bishop_top_left(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_top_position(temp)
#             temp = self.get_leftTop_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def bishop_top_right(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_top_position(temp)
#             temp = self.get_rightTop_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def generate_bishop_moves(self, position):
#         move = []
#         move += [self.bishop_bottom_left(position)]
#         move += [self.bishop_middle_left(position)]
#         move += [self.bishop_top_left(position)]
#         move += [self.bishop_top_right(position)]
#         move += [self.bishop_middle_right(position)]
#         move += [self.bishop_bottom_right(position)]
#         return move
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_bishop_moves(self.position)
#         else:
#             return self.generate_bishop_moves(position)
#
#
# class Rook(Pieces):
#     def __init__(self, team, position):
#         super(Rook, self).__init__(team, ROOK, position)
#
#     def rook_bottom(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_down_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def rook_bottom_left(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_leftDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def rook_bottom_right(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_rightDown_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def rook_top(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_top_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def rook_top_left(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_leftTop_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def rook_top_right(self, pos):
#         list_of_action = []
#         temp = pos
#         while temp is not None:
#             temp = self.get_rightTop_position(temp)
#             list_of_action.append(temp)
#         return list_of_action
#
#     def generate_rook_moves(self, pos):
#         move = []
#         move += [self.rook_bottom(pos)]
#         move += [self.rook_bottom_left(pos)]
#         move += [self.rook_top_left(pos)]
#         move += [self.rook_top(pos)]
#         move += [self.rook_top_right(pos)]
#         move += [self.rook_bottom_right(pos)]
#         return move
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_rook_moves(self.position)
#         else:
#             return self.generate_rook_moves(position)
#
#
# class Queen(Bishop, Rook):
#     def __init__(self, team, position):
#         Pieces.__init__(self, team, QUEEN, position)
#         # super(Queen, self).__init__(team,QUEEN,position)
#
#     def generate_queen_moves(self, position):
#         move = []
#         move += self.generate_rook_moves(position)
#         move += self.generate_bishop_moves(position)
#         return move
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_queen_moves(self.position)
#         else:
#             return self.generate_queen_moves(position)
#
#
# class King(Pieces):
#     def __init__(self, team, position):
#         super(King, self).__init__(team, KING, position)
#
#     def generate_king_moves(self, position):
#         return list(map(lambda x: [x], self.get_positon_around(position)))
#
#     def generate_moves(self, position=None):
#         if (position is None):
#             return self.generate_king_moves(self.position)
#         else:
#             return self.generate_king_moves(position)
