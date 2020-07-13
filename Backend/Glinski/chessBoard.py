from chessPieces import *

default_state = {
    "white": {
        "pawn": ['B2', 'C3', 'D4', 'E5', 'F4', 'G3', 'H2'],
        "knight": ['C1', 'G1'],
        "bishop": ['E1', 'E2', 'E3' ],
        "rook": ['B1', 'H1'],
        "queen": ['D1'],
        "king": ['F1'],
    },
    "black": {
        "pawn": ['B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
        "knight": ['C8', 'G8'],
        "bishop": ['E8', 'E9', 'E10'],
        "rook": ['B7', 'H7'],
        "queen": ['D9'],
        "king": ['F9'],
    }
}

class ChessBoard:
    def __init__(self, state=default_state):
        self.state = self.update_state(state)

    def get_state(self,kind_of_state='COMPLEX'):
        if(kind_of_state == 'SIMPLE'):
            new_state = {
                "white": {
                    "pawn": [],
                    "knight": [],
                    "bishop": [],
                    "rook": [],
                    "queen": [],
                    "king": [],
                },
                "black": {
                    "pawn": [],
                    "knight": [],
                    "bishop": [],
                    "rook": [],
                    "queen": [],
                    "king": [],
                }
            }
            for team in self.state:
                for kind in self.state[team]:
                    for piece in self.state[team][kind]:
                        pos = piece.get_position()
                        new_state[team][kind].append(pos)
            return new_state
        elif kind_of_state=='COMPLEX':
            return self.state

    def update_state(self, new_state):
        temp_state = {
            "white": {
                "pawn": [],
                "knight": [],
                "bishop": [],
                "rook": [],
                "queen": [],
                "king": [],
            },
            "black": {
                "pawn": [],
                "knight": [],
                "bishop": [],
                "rook": [],
                "queen": [],
                "king": [],
            }
        }
        for team in new_state:
            for kind_of_chess in new_state[team]:
                for position in new_state[team][kind_of_chess]:
                    if (kind_of_chess == "pawn"):
                        temp_state[team][kind_of_chess].append(Pawn(team.upper(), position))
                    elif kind_of_chess == "knight":
                        temp_state[team][kind_of_chess].append(Knight(team.upper(), position))
                    elif kind_of_chess == "bishop":
                        temp_state[team][kind_of_chess].append(Bishop(team.upper(), position))
                    elif kind_of_chess == "rook":
                        temp_state[team][kind_of_chess].append(Rook(team.upper(), position))
                    elif kind_of_chess == 'queen':
                        temp_state[team][kind_of_chess].append(Queen(team.upper(), position))
                    elif kind_of_chess == 'king':
                        temp_state[team][kind_of_chess].append(King(team.upper(), position))
        return temp_state

    def select_piece_at(self,position):#make sure position is empty
        for team in self.state:
            for kind in self.state[team]:
                for piece in self.state[team][kind]:
                    if piece.get_position() == position:
                        return piece
        return None

    def render(self, team="all"):
        if (team == 'all'):
            for team in self.state:
                for kind in self.state[team]:
                    for piece in self.state[team][kind]:
                        print(piece)
        elif team == WHITE:
            for kind in self.state["white"]:
                for piece in self.state["white"][kind]:
                    print(piece)
        elif team == BLACK:
            for kind in self.state["black"]:
                for piece in self.state["black"][kind]:
                    print(piece)

    def get_locations_of(self, team=None):
        locations = []
        if team == None:
            return None
        for kind in self.state[team.lower()]:
            for piece in self.state[team.lower()][kind]:
                locations.append(piece.get_position())
        return locations

    def is_empty_location(self, position):
        if (not self.is_location_valid(position)):
            return None
        white = self.get_locations_of(WHITE)
        black = self.get_locations_of(BLACK)
        if position in white or position in black:
            return False
        else:
            return True

    def validate_pawns_move(self, piece):
        team = piece.get_team()
        white = self.get_locations_of(WHITE)
        black = self.get_locations_of(BLACK)
        moveable = piece.generate_moves()
        lom = []
        if (team == WHITE):
            if (self.is_empty_location(moveable[0][0])):
                lom.append(moveable[0][0])
            for i in moveable[1]:
                if i in black:
                    lom.append(i)
        elif team == BLACK:
            if (self.is_empty_location(moveable[0][0])):
                lom.append(moveable[0][0])
            for i in moveable[1]:
                if i in white:
                    lom.append(i)
        return lom

    def validate_knight_moves(self, piece):
        team = piece.get_team()
        white = self.get_locations_of(WHITE)
        black = self.get_locations_of(BLACK)
        moveable = piece.generate_moves()
        lom = []
        if team == WHITE:
            for i in moveable:
                if (i is None or i in white):
                    continue
                lom.append(i)
        elif team == BLACK:
            for i in moveable:
                if (i is None or i in black):
                    continue
                lom.append(i)
        return lom

    def validate_bishop_rook_queen_king_moves(self, piece):
        team = piece.get_team()
        white = self.get_locations_of(WHITE)
        black = self.get_locations_of(BLACK)
        moveable = piece.generate_moves()
        lom = []
        # print(moveable)
        if team == WHITE:
            for direction in moveable:
                for i in direction:
                    if(i in black):
                        lom.append(i)
                        break
                    if (i is None or i in white):
                        break
                    lom.append(i)
        elif team == BLACK:
            for direction in moveable:
                for i in direction:
                    if (i in white):
                        lom.append(i)
                        break
                    if (i is None or i in black):
                        break
                    lom.append(i)
        return lom

    def validate_moves(self,piece):
        type = piece.get_type()
        if(type == PAWN):
            return self.validate_pawns_move(piece)
        elif type == KNIGHT:
            return self.validate_knight_moves(piece)
        elif type==KING or type==ROOK or type == BISHOP or type == QUEEN:
            return self.validate_bishop_rook_queen_king_moves(piece)
        return []

    def is_location_valid(self,position):
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

    def is_done(self):
        black_king = self.state["black"]["king"]
        white_king = self.state["white"]["king"]
        if(len(black_king)+len(white_king)==2):
            return None
        elif(len(black_king)==0):
            return WHITE
        elif(len(white_king)==0):
            return BLACK
        return None

    def get_action_at(self,position):
        # print(position)
        position = position.upper()
        if(self.is_empty_location(position)):
            return None
        else:
            piece = self.select_piece_at(position)
            # print(position)
            moves = self.validate_moves(piece)
            moves = list(map(lambda x:'{}->{}'.format(position,x),moves))
            return moves

    def perform_move(self,move):
        temp = self.new_state_from_move(move,'SIMPLE')
        self.state=self.update_state(temp)
        return

    def new_state_from_move(self,move,kind_of_state='COMPLEX'):
        new_state = {
            "white": {
                "pawn": [],
                "knight": [],
                "bishop": [],
                "rook": [],
                "queen": [],
                "king": [],
            },
            "black": {
                "pawn": [],
                "knight": [],
                "bishop": [],
                "rook": [],
                "queen": [],
                "king": [],
            }
        }
        move=move.upper()
        original=move.split('->')[0]
        destination=move.split('->')[1]
        blacks = self.get_locations_of(BLACK)
        whites = self.get_locations_of(WHITE)
        piece = self.select_piece_at(original)
        # print(self.state, piece)
        if(piece is None):
            # print(self.state,piece)
            return None
        team = piece.get_team()
        atk=False
        if(move in self.get_action_at(original)):
            if(team == BLACK):
                if(destination in whites): #attack move
                    atk = True
            elif team == WHITE:
                if (destination in blacks):  # attack move
                    atk = True

            for team in self.state:
                for kind in self.state[team]:
                    for piece in self.state[team][kind]:
                        pos = piece.get_position()
                        if(atk and pos==destination):
                            continue
                        if(pos ==original):
                            pos = destination
                        new_state[team][kind].append(pos)

        if(kind_of_state=='SIMPLE'):
            return new_state
        elif kind_of_state =='COMPLEX':
            return self.update_state(new_state)
            # return new_state
        return None

    def get_actions_of(self,team=BLACK):
        if(team==BLACK):
            locs = self.get_locations_of(BLACK)
            locs = list(map(self.get_action_at,locs))
        elif team == WHITE:
            locs = self.get_locations_of(WHITE)
            locs = list(map(self.get_action_at, locs))
            # print(locs)
        answ = []
        for i in locs:
            answ+=i
        return answ
    # def get_info(self):


    # def get_action(self,team=BLACK):




