from utils import Object
from position import Position

class Piece:    
    def setPosition (self, position):
        self.position = position
    def detachPosition (self):
        self.position = None
    def __init__(self, game, color, position = None):
        self.position = position
        self.game = game
        self.color = color
        self.name = type(self).__name__
        self.strikes = 0

    def isValid(self, position):
        piece = self.game.occupation(position)
        if piece == None:
            valid = True
        elif piece.color == self.color:
            print ( f'Moving to own piece {piece}')
            valid = False
        else:
            print (f'Would take piece {piece}')
            valid = True
        return Object(valid=valid, occupation=piece)
    def isValidMove(self):
        raise Exception(f'function not defined for {type(self).__name__}')


    def move_to(self, A1Str):
        return self.move(Position(self.game,  A1Str))

    def move(self, position):
        if self.position == None:
            raise Exception(f'position not defined for {type(self).__name__}')
        target_square = self.isValid(position)
        move_effect= self.isValidMove(position)
        if (target_square.valid #the chessboard allows this move : the square exists and is not occupied by own
            and move_effect.valid):# this piece specialization allows for it 
                self.game.move(self, position, target_square.occupation,move_effect.effect)
                self.setPosition(position)
                self.strikes += 1
        else:
            raise Exception(f'{str(self)} cannot move from {str(self.position)} to {str(position)}, occupied by {str(target_square.occupation)} ')

    def __str__(self):
        return self.game.representation[self.name][self.color]
        #return f'{self.color}{self.name}{self.position}'

    def movesOnDownUpDiagonal(self):
        if self.position == None:
            raise Exception(f'position not defined for {type(self).__name__}')
        move_deltas = []
        maxmins = Position.movesMaxMins(self.position)
        for i in range (min(self.position.rowNum, self.position.colNum), maxmins.upright_delta_diag + 1): #moves on diag parallel to A1 - H8
           if i != 0 :
                occ = self.game.occupation(Position.nums2A1Str((self.position.colNum + i, self.position.rowNum + i)))
                if occ == None or occ.color != self.color: 
                   move_deltas.append((self.position.colNum + i, self.position.rowNum + i)) 
                if occ != None: #we stop here
                   break
        for i in range (maxmins.downleft_delta_diag, maxmins.upright_delta_diag + 1): #moves on diag parallel to A1 - H8
        if i != 0 :
            occ = self.game.occupation(Position.nums2A1Str((self.position.colNum + i, self.position.rowNum + i)))
            if occ == None or occ.color != self.color: 
                move_deltas.append((self.position.colNum + i, self.position.rowNum + i)) 
            if occ != None: #we stop here
                break

        return move_deltas

    def movesOnUpDownDiagonal(self):
        if self.position == None:
            raise Exception(f'position not defined for {type(self).__name__}')
        move_deltas = []
        maxmins = Position.movesMaxMins(self.position)

        for i in range (maxmins.upleft_delta_diag, maxmins.downright_delta_diag + 1): #moves on diag parallel A8 - H1
           if i != 0 : move_deltas.append((self.position.colNum + i, self.position.rowNum - i)) 

        return move_deltas

    def movesOnColumn(self):
        if self.position == None:
            raise Exception(f'position not defined for {type(self).__name__}')
        move_deltas = []
        maxmins = Position.movesMaxMins(self.position)

        for i in range (maxmins.down_delta_row, maxmins.up_delta_row + 1): #moves on same col
           if i != 0 : move_deltas.append((self.position.colNum, self.position.rowNum + i))

        return move_deltas

    def movesOnRow(self):
        if self.position == None:
            raise Exception(f'position not defined for {type(self).__name__}')
        move_deltas = []
        maxmins = Position.movesMaxMins(self.position)

        for i in range (maxmins.left_delta_col, maxmins.right_delta_col + 1): #moves on same row
            if i != 0 : move_deltas.append((self.position.colNum + i, self.position.rowNum)) 

        return move_deltas
    