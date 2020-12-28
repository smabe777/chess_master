from utils import Object
from piece import Piece
from position import Position
from chess import Chess

class Pawn (Piece):
    def isValidMove(self, position):
        if self.position == None:
            raise Exception(f'no position defined')
        en_passant = self.detectEnPassant()
        if en_passant != None :
            effect = lambda: self.game.remove(en_passant[0])
        else: effect = None

        return Object(valid = len (list(filter (lambda y: y == str(position), [str(x) for x in self.listValidMoves()]))) == 1,
            effect = effect)

    def startingPosition(self):
        if self.position == None : return False
        return (self.strikes == 0 
            and ((self.color == Chess.WHITE and self.position.rowNum == 2) or (self.color == Chess.BLACK and self.position.rowNum == 7)))

    def detectEnPassant(self):
        if self.game.last_move != None:
            last_piece = self.game.last_move[0]
            last_position = self.game.last_move[1]
            row_diff = abs(last_piece.position.rowNum - last_position.rowNum)
            col_diff = abs(self.position.colNum - last_position.colNum) 

            if type(last_piece).__name__ == 'Pawn' and self.position.rowNum == last_piece.position.rowNum and abs(col_diff) == 1 and row_diff == 2: #last move needs to be an opponent pawn 'jumping' at the start
                    if self.color == self.game.WHITE:
                        new_rowNum = last_position.rowNum - 1
                    else:
                        new_rowNum = last_position.rowNum + 1
                
                    return (last_piece, Position(self.game, Position.nums2A1Str(last_position.colNum, new_rowNum)))
        return None

        
    def listValidMoves(self):
        moves =[]
        if self.color == self.game.WHITE :
            turnFactor = 1
        else:
            turnFactor = -1
        
        if (self.game.squareDoesExist(self.position.col, Position.num2row(self.position.rowNum + 1 * turnFactor))
            and self.game.occupation(Position.strings2A1Str(self.position.col, Position.num2row(self.position.rowNum + 1* turnFactor))) == None):
            moves.append(Position(self.game, Position.strings2A1Str(self.position.col, Position.num2row(self.position.rowNum + 1* turnFactor))))
        
        if (self.startingPosition()
            and self.game.occupation(Position.strings2A1Str(self.position.col, Position.num2row(self.position.rowNum + 2* turnFactor))) == None
            and self.game.occupation(Position.strings2A1Str(self.position.col, Position.num2row(self.position.rowNum + 1* turnFactor))) == None) : 
            moves.append(Position(self.game, Position.strings2A1Str(self.position.col, Position.num2row(self.position.rowNum + 2* turnFactor))))

        try:
            prospect_move_diag_left = Position(self.game, Position.strings2A1Str(Position.num2col(self.position.colNum - 1* turnFactor), Position.num2row(self.position.rowNum + 1* turnFactor)))
            move_diag_left = self.isValid( prospect_move_diag_left)
            if move_diag_left.valid and move_diag_left.occupation != None : #there is an opponent
                moves.append( prospect_move_diag_left)
        except: #Exception on Invalid Position
            pass
        
        try:
            prospect_move_diag_right = Position(self.game, Position.strings2A1Str(Position.num2col(self.position.colNum + 1* turnFactor), Position.num2row(self.position.rowNum + 1* turnFactor)))       
            move_diag_right = self.isValid(prospect_move_diag_right)  
            if  move_diag_right.valid and  move_diag_right.occupation != None : #there is an opponent
                moves.append(prospect_move_diag_right)
        except: #Exception on Invalid Position
            pass

        en_passant = self.detectEnPassant()
        if en_passant != None:
            moves.append(en_passant[1])
        return moves
