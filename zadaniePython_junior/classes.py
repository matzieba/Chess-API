from szachownica import chessboard
from moves import (
    moves_generator,
    moves_generator_rock,
    moves_generator_bischop,
    moves_generator_knight,
    moves_generator_pawn,
)
from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, currentField):
        self.currentField = currentField

    @abstractmethod
    def list_available_moves(self):
        for sub_list in chessboard:
            if self.currentField in sub_list:
                return [chessboard.index(sub_list),
                        sub_list.index(self.currentField)]
        raise ValueError("'{char}' is not in list".
                         format(char=self.currentField))

    def validate_move(self, dest_field):
        moves = self.list_available_moves()
        return moves


class King(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator(index, chessboard, 2)
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"


class Queen(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator(index, chessboard, len(chessboard))
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"


class Rook(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator_rock(index, chessboard, len(chessboard))
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"


class Bischop(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator_bischop(index, chessboard, len(chessboard))
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"


class Knight(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator_knight(index, chessboard)
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"


class Pawn(Figure):
    def list_available_moves(self):
        index = super().list_available_moves()
        moves = moves_generator_pawn(index, chessboard)
        return moves

    def validate_move(self, dest_field):
        moves = super().validate_move(dest_field)
        if dest_field in moves:
            return "Move is valid"
        else:
            return "Move is invalid"
