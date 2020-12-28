from utils import Object
from piece import Piece
from chess import Chess
from position import Position

class Queen(Piece):
    def isValidMove(self, position):
        if self.position == None:
            raise Exception(f'no position defined')
        if not super(Queen, self).isValid(position).valid:
            return False
        new_row = position.rowNum
        new_col = position.colNum
        curr_row = self.position.rowNum
        curr_col = self.position.colNum
        delta_row = abs(new_row - curr_row)
        delta_col = abs(new_col - curr_col)
        if delta_row == 0 or delta_col == 0 or delta_row == delta_col:
            return Object(valid = True, effect = None)
        else:
            print ('Illegal position')
            return Object(valid = False, effect = None)
    def listValidMoves(self):
        moves = []
        move_deltas =[]
        move_deltas += self.movesOnColumn()
        move_deltas += self.movesOnRow()
        move_deltas += self.movesOnDownUpDiagonal()
        move_deltas += self.movesOnUpDownDiagonal()

        for delta in move_deltas:
            if self.game.squareDoesExist(Position.num2col(delta[0]), Position.num2row(delta[1])):
                moves.append(Position(self.game, Position.nums2A1Str(delta[0], delta[1])))
        return moves

