from utils import Object
from piece import Piece
from chess import Chess
from position import Position

class King(Piece):
    def isValidMove(self, position):
        if not super(King, self).isValid(position).valid:
            return Object(valid = False, effect = None)
        new_row = position.rowNum
        new_col = position.colNum
        curr_row = self.position.rowNum
        curr_col = self.position.colNum
        if abs(new_row - curr_row) <= 1 and abs(new_col - curr_col) <= 1:
            return Object(valid = True, effect = None)
        else:
            print ('Illegal position')
            return Object(valid = False, effect = None)
    def listValidMoves(self):
        moves =[]
        move_deltas = [(self.position.col, Position.num2row(self.position.rowNum + 1)),#north
        (self.position.col, Position.num2row(self.position.rowNum - 1)),#south
        (Position.num2col(self.position.colNum + 1), self.position.row), #east
        (Position.num2col(self.position.colNum - 1), self.position.row), #west
        (Position.num2col(self.position.colNum + 1), Position.num2row(self.position.rowNum + 1)), #northeast
        (Position.num2col(self.position.colNum - 1), Position.num2row(self.position.rowNum + 1)), #northwest
        (Position.num2col(self.position.colNum + 1), Position.num2row(self.position.rowNum - 1)), #southeast
        (Position.num2col(self.position.colNum - 1), Position.num2row(self.position.rowNum - 1)) #southwest
        ]
        for delta in move_deltas:
            if self.game.squareDoesExist(delta[0], delta[1]):
                moves.append(Position(self.game, Position.strings2A1Str(delta[0], delta[1])))
        return moves
