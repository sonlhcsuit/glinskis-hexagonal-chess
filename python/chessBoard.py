import numpy as np
from Piece import *
from utils import encode_notation, decode_notation

default_state = {
    "white": {
        "pawn": ['B2', 'C3', 'D4', 'E5', 'F4', 'G3', 'H2'],
        "knight": ['C1', 'G1'],
        "bishop": ['E1', 'E2', 'E3'],
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
