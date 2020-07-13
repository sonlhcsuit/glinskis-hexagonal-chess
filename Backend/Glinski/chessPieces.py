PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING = "PAWN", "KNIGHT", "BISHOP", "ROOK", "QUEEN", "KING"
WHITE, BLACK = "WHITE", "BLACK"

class Pieces(object):
    def __init__(self, team, type, position):
        self.position = position  # string
        self.type = type  # string
        self.team = team  # string
        self.moveable = []
        coefficent = 1 if team==WHITE else -1
        if (type == PAWN):
            self.value = coefficent*10
        elif type == KNIGHT:
            self.value = coefficent*30
        elif type == BISHOP:
            self.value = coefficent*60
        elif type == ROOK:
            self.value = coefficent*100
        elif type == QUEEN:
            self.value = coefficent*250
        elif type == KING:
            self.value = coefficent*900

    def valid_position(self, position):
        if position[0] == 'A' or position[0] == 'I':
            return int(position[1:]) <= 6 and int(position[1:]) >= 1
        elif position[0] == 'B' or position[0] == 'H':
            return int(position[1:]) <= 7 and int(position[1:]) >= 1
        elif position[0] == 'C' or position[0] == 'G':
            return int(position[1:]) <= 8 and int(position[1:]) >= 1
        elif position[0] == 'D' or position[0] == 'F':
            return int(position[1:]) <= 9 and int(position[1:]) >= 1
        elif position[0] == 'E':
            return int(position[1:]) <= 10 and int(position[1:]) >= 1
        else:
            return False
    def get_position(self):
        return self.position
    def get_value(self):
        return self.value
    def get_team(self):
        return self.team
    def get_type(self):
        return self.type

    def get_moveable(self):
        return self.moveable

    def get_positon_around(self, current_pos):
        if (current_pos == None):
            return [None, None, None, None, None, None]
        col = current_pos[0]
        row = int(current_pos[1:])
        arround_pos = []
        if (col == 'E'):
            down = '{}{}'.format(col, row - 1)
            leftDown = '{}{}'.format(chr(ord(col) - 1), row - 1)
            leftTop = '{}{}'.format(chr(ord(col) - 1), row)
            top = '{}{}'.format(col, row + 1)
            rightTop = '{}{}'.format(chr(ord(col) + 1), row)
            rightDown = '{}{}'.format(chr(ord(col) + 1), row - 1)
            arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
            arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
        if (col < 'E'):
            down = '{}{}'.format(col, row - 1)
            leftDown = '{}{}'.format(chr(ord(col) - 1), row - 1)
            leftTop = '{}{}'.format(chr(ord(col) - 1), row)
            top = '{}{}'.format(col, row + 1)
            rightTop = '{}{}'.format(chr(ord(col) + 1), row + 1)
            rightDown = '{}{}'.format(chr(ord(col) + 1), row)
            arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
            arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
        if (col > 'E'):
            down = '{}{}'.format(col, row - 1)
            leftDown = '{}{}'.format(chr(ord(col) - 1), row)
            leftTop = '{}{}'.format(chr(ord(col) - 1), row + 1)
            top = '{}{}'.format(col, row + 1)
            rightTop = '{}{}'.format(chr(ord(col) + 1), row)
            rightDown = '{}{}'.format(chr(ord(col) + 1), row - 1)
            arround_pos = [down, leftDown, leftTop, top, rightTop, rightDown]
            arround_pos = list(map(lambda x: x if self.valid_position(x) else None, arround_pos))
        return arround_pos

    def get_down_position(self, position):
        return self.get_positon_around(position)[0]

    def get_leftDown_position(self, position):
        return self.get_positon_around(position)[1]

    def get_leftTop_position(self, position):
        return self.get_positon_around(position)[2]

    def get_top_position(self, position):
        return self.get_positon_around(position)[3]

    def get_rightTop_position(self, position):
        return self.get_positon_around(position)[4]

    def get_rightDown_position(self, position):
        return self.get_positon_around(position)[5]
    def generate_moves(self,position):
        return position
    def get_info(self):
        return (self.team,self.type,self.position,self.value)
    def __str__(self):
        # return self.get_info()
        return '{} {} {} {}'.format(self.team, self.type, self.position, self.value)

    def __repr__(self):
        return self.__str__()

class Pawn(Pieces):
    def __init__(self, team, position):
        super(Pawn, self).__init__(team, PAWN, position)

    def generate_pawn_moves(self,position):
        if(self.team == WHITE):
            lt = self.get_leftTop_position(position)
            t = self.get_top_position(position)
            rt = self.get_rightTop_position(position)
            self.moveable = [[t],[lt, rt]]
            return self.moveable
        elif self.team == BLACK:
            ld = self.get_leftDown_position(position)
            d = self.get_down_position(position)
            rd = self.get_rightDown_position(position)
            self.moveable = [[d], [ld, rd]]
            return self.moveable

    def generate_moves(self,position=None):
        if(position is None):
            return self.generate_pawn_moves(self.position)
        else:
            return self.generate_pawn_moves(position)

class Knight(Pieces):
    def __init__(self, team, position):
        super(Knight, self).__init__(team, KNIGHT, position)

    def generate_knight_moves(self,position):
        move = []
        # left bottom
        tempPos = self.get_down_position(position)
        tempPos = self.get_leftDown_position(tempPos)
        move.append(self.get_down_position(tempPos))
        move.append(self.get_leftDown_position(tempPos))
        # right bottom
        tempPos = self.get_down_position(position)
        tempPos = self.get_rightDown_position(tempPos)
        move.append(self.get_down_position(tempPos))
        move.append(self.get_rightDown_position(tempPos))
        # left middle
        tempPos = self.get_leftDown_position(position)
        tempPos = self.get_leftTop_position(tempPos)
        move.append(self.get_leftDown_position(tempPos))
        move.append(self.get_leftTop_position(tempPos))
        # right middle
        tempPos = self.get_rightDown_position(position)
        tempPos = self.get_rightTop_position(tempPos)
        move.append(self.get_rightDown_position(tempPos))
        move.append(self.get_rightTop_position(tempPos))
        # left top
        tempPos = self.get_top_position(position)
        tempPos = self.get_leftTop_position(tempPos)
        move.append(self.get_leftTop_position(tempPos))
        move.append(self.get_top_position(tempPos))
        # right top
        tempPos = self.get_top_position(position)
        tempPos = self.get_rightTop_position(tempPos)
        move.append(self.get_top_position(tempPos))
        move.append(self.get_rightTop_position(tempPos))
        return move
    def generate_moves(self,position=None):
        if (position is None):
            return self.generate_knight_moves(self.position)
        else:
            return self.generate_knight_moves(position)

class Bishop(Pieces):
    def __init__(self, team, position):
        super(Bishop, self).__init__(team, BISHOP, position)

    def bishop_bottom_left(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_down_position(temp)
            temp = self.get_leftDown_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def bishop_bottom_right(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_down_position(temp)
            temp = self.get_rightDown_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def bishop_middle_left(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_leftTop_position(temp)
            temp = self.get_leftDown_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def bishop_middle_right(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_rightTop_position(temp)
            temp = self.get_rightDown_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def bishop_top_left(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_top_position(temp)
            temp = self.get_leftTop_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def bishop_top_right(self, pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_top_position(temp)
            temp = self.get_rightTop_position(temp)
            list_of_action.append(temp)
        return list_of_action

    def generate_bishop_moves(self, position):
        move = []
        move += [self.bishop_bottom_left(position)]
        move += [self.bishop_middle_left(position)]
        move += [self.bishop_top_left(position)]
        move += [self.bishop_top_right(position)]
        move += [self.bishop_middle_right(position)]
        move += [self.bishop_bottom_right(position)]
        return move

    def generate_moves(self, position=None):
        if (position is None):
            return self.generate_bishop_moves(self.position)
        else:
            return self.generate_bishop_moves(position)

class Rook(Pieces):
    def __init__(self,team,position):
        super(Rook, self).__init__(team,ROOK,position)

    def rook_bottom(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_down_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def rook_bottom_left(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_leftDown_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def rook_bottom_right(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_rightDown_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def rook_top(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_top_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def rook_top_left(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_leftTop_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def rook_top_right(self,pos):
        list_of_action = []
        temp = pos
        while temp is not None:
            temp = self.get_rightTop_position(temp)
            list_of_action.append(temp)
        return list_of_action
    def generate_rook_moves(self,pos):
        move = []
        move += [self.rook_bottom(pos)]
        move += [self.rook_bottom_left(pos)]
        move += [self.rook_top_left(pos)]
        move += [self.rook_top(pos)]
        move += [self.rook_top_right(pos)]
        move += [self.rook_bottom_right(pos)]
        return move

    def generate_moves(self, position=None):
        if (position is None):
            return self.generate_rook_moves(self.position)
        else:
            return self.generate_rook_moves(position)

class Queen(Bishop,Rook):
    def __init__(self,team,position):
        Pieces.__init__(self,team,QUEEN,position)
        # super(Queen, self).__init__(team,QUEEN,position)

    def generate_queen_moves(self,position):
        move = []
        move += self.generate_rook_moves(position)
        move += self.generate_bishop_moves(position)
        return move

    def generate_moves(self, position=None):
        if (position is None):
            return self.generate_queen_moves(self.position)
        else:
            return self.generate_queen_moves(position)

class King(Pieces):
    def __init__(self,team,position):
        super(King, self).__init__(team,KING,position)
    def generate_king_moves(self,position):
        return list(map(lambda x:[x],self.get_positon_around(position)))

    def generate_moves(self, position=None):
        if (position is None):
            return self.generate_king_moves(self.position)
        else:
            return self.generate_king_moves(position)
