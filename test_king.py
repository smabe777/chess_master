from test import Test
from position import Position
from king import King
from chess import Chess

class Test_King (Test):
    def __init__(self, game):
        self.game = game
        self.king = King(game, Chess.WHITE, Position(game,'E5'))
    def test_valid_move(self):
        self.t_assert("K-E5 -> E6 is OK", self.king.isValidMove(Position(self.game,'E6')).valid)
        self.t_assert("K-E5 -> E7 is Not OK", not self.king.isValidMove(Position(self.game,'E7')).valid)
        self.t_assert("K-E5 -> A5 is Not OK", not self.king.isValidMove(Position(self.game,'A5')).valid)
    def test_occupied(self):
        origKing = self.game.occupation (Position(self.game, 'E1'))
        print(self.king)
        self.t_assert("K-E1 -> E2 is Not OK", not origKing.isValidMove(Position(self.game,'E2')).valid)
    def test_get_valid_moves(self):
        moves = self.king.listValidMoves()
        self.t_assert("8 possible moves", len(moves) == 8 )
        for move in moves:
            print(move)
    def test(self):
        self.test_valid_move()
        self.test_occupied()
        self.test_get_valid_moves()