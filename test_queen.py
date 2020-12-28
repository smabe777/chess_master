from test import Test
from position import Position
from queen import Queen
from chess import Chess

class Test_Queen (Test):
    def __init__(self, game):
        self.game = game
        self.position = Position(self.game,'E5')
        self.game.empty_board()
        self.game.place_piece(Queen(self.game, Chess.WHITE), self.position)
        self.queen = self.game.occupation(self.position)

    def test_valid_move(self):
        self.t_assert("Q-E5 -> G7 is OK", self.queen.isValidMove(Position(self.game,'G7')).valid)
        self.t_assert("Q-E5 -> B2 is OK", self.queen.isValidMove(Position(self.game,'B2')).valid)
        self.t_assert("Q-E5 -> E1 is OK", self.queen.isValidMove(Position(self.game,'E1')).valid)
        self.t_assert("Q-E5 -> A5 is OK", self.queen.isValidMove(Position(self.game,'A5')).valid)
        self.t_assert("Q-E5 -> B6 is Not OK", not self.queen.isValidMove(Position(self.game,'B6')).valid)
        self.t_assert("Q-E5 -> A2 is Not OK", not self.queen.isValidMove(Position(self.game,'A2')).valid)
        self.place_queen( Position(self.game,'H1'))
        self.t_assert("Q-H2 -> B7 is OK", self.queen.isValidMove(Position(self.game,'B7')).valid)

    def place_queen(self, position):
        self.position = position
        self.queen = self.game.place_piece(self.queen, self.position)
    def test_get_valid_moves(self):
        self.place_queen( Position(self.game,'E5'))
        moves = self.queen.listValidMoves()
        self.t_assert("E5 : 27 possible moves", len(moves) == 27)
        self.place_queen( Position(self.game,'G5'))
        moves = self.queen.listValidMoves()
        self.t_assert("G5 : at least 21 possible moves", len(moves) >= 21)
        self.place_queen( Position(self.game,'H2'))
        moves = self.queen.listValidMoves()
        self.t_assert("H2 : at least 21 possible moves", len(moves) >= 21)

    def test_best_position(self):
        results=[]
        for colNum in range (1, 9):
            for rowNum in range(1, 9):
                self.position = Position(self.game, Position.nums2A1Str(colNum,rowNum))
                self.place_queen( self.position)
                moves = self.queen.listValidMoves()
                results.append((str(self.position), len(moves)))
        best_results = list(filter(lambda x: x[1] >= 27, results))
        self.game.empty_board()
        for result in best_results:
            print (f'Queen in {result[0]}')
            self.game.add_piece(Queen(self.game,Chess.WHITE), Position(self.game, result[0]))
            #self.game.chessBoard()
        self.t_assert("4 positions with 27 moves", len(best_results) == 4)

    def test(self):
        self.test_valid_move()
        self.test_get_valid_moves()
        self.test_best_position()

