from chess import Chess
from position import Position

class Match:
    def __init__(self):
        self.game = Chess()
        self.game.init_board()
        self.game.chessBoard()
    def move (self, from_position, to_position):
        piece = self.game.occupation(from_position)
        if piece == None : 
            print(f'no piece in {from_position}')
            return False
        piece.move(Position(self.game, to_position))
        return True

m = Match()
Ok = True
def exec_turn(ok, move):
    if ok == True :
        positions = move.split('-')
        return m.move(positions[0], positions[1])
    return False

if Ok: Ok = exec_turn(Ok, 'E2-E4')
if Ok: Ok = exec_turn(Ok, 'E7-E5')
if Ok: Ok = exec_turn(Ok, 'D1-H5')
if Ok: Ok = exec_turn(Ok, 'F7-F6')
if Ok: Ok = exec_turn(Ok, 'H5-H8')