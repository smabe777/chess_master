from test import Test
from position import Position
from pawn import Pawn
from chess import Chess

class Test_Pawn(Test):
    def __init__(self, game):
        self.game = game
        self.pawn = Pawn(self.game, Chess.WHITE)
    def test_is_valid_move(self):
        self.game.empty_board()
        p = self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'H6'))
        self.t_assert('black pawn H6 can go to H5', p.isValidMove(Position(self.game, 'H5')).valid)
        self.t_assert('black pawn H6 cannot go to H4', not p.isValidMove(Position(self.game, 'H4')).valid)
        self.t_assert('black pawn H6 cannot go to H7', not p.isValidMove(Position(self.game, 'H7')).valid)
        self.t_assert('black pawn H6 cannot go to G6', not p.isValidMove(Position(self.game, 'G6')).valid)
        self.game.place_piece(Pawn(self.game, Chess.WHITE), Position(self.game, 'G5'))
        self.t_assert('black pawn H6 can take white pawn in G5', p.isValidMove(Position(self.game, 'G5')).valid)

    def test_starting(self):
        self.game.empty_board()
        self.game.place_piece(self.pawn, Position(self.game,'E2'))
        moves = self.pawn.listValidMoves()
        self.t_assert('pawn starting in E2 has 2 possible moves', len(moves) == 2)
        print([str(x) for x in moves])
    def test_classic_moves(self):
        self.game.empty_board()
        self.game.place_piece(self.pawn, Position(self.game,'E5'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'D6'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'F6'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'D4'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game,'F4'))
        self.game.chessBoard()
        moves = self.pawn.listValidMoves()
        self.t_assert('pawn in E5 with opponents in D6,F6,D4, F4 has 3 possible moves', len(moves) == 3)
        print([str(x) for x in moves])
    def test_starting_black(self):
        self.game.empty_board()
        p = self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game,'E7'))
        moves = p.listValidMoves()
        self.t_assert('Black pawn starting in E7 has 2 possible moves', len(moves) == 2)
        print([str(x) for x in moves])
    def test_back(self):
        self.game.empty_board()
        self.game.place_piece(self.pawn, Position(self.game,'E5'))
        self.t_assert('pawn cannot go backwards', not self.pawn.isValidMove(Position(self.game, 'E4')).valid)
    def test_no_jump(self):
        self.game.empty_board()
        self.game.place_piece(self.pawn, Position(self.game,'E2'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'E3'))
        self.t_assert('pawn cannot jump - E2 to E4, with piece in E3', not self.pawn.isValidMove(Position(self.game, 'E4')).valid)
        moves = self.pawn.listValidMoves()
        print([str(x) for x in moves])
    def test_cannot_take_vertically_after_double(self):
        self.game.empty_board()
        self.game.place_piece(self.pawn, Position(self.game,'E2'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'E4'))
        self.t_assert('pawn cannot take in front after double start, E2-E4 with piece in E4', not self.pawn.isValidMove(Position(self.game, 'E4')).valid)
        moves = self.pawn.listValidMoves()
        print([str(x) for x in moves])
    def setup_test_1(self):
        self.game.empty_board()
        wp = self.game.place_piece(Pawn(self.game, Chess.WHITE), Position(self.game,'F4'))
        bp = self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'E7'))
        self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'G6'))
        wp.move(Position(self.game, 'F5'))
        bp.move(Position(self.game, 'E5'))
        self.game.chessBoard()
        return wp
    def test_en_passant(self):
        wp = self.setup_test_1()
        self.t_assert('en passant : pawn in F5 can take black pawn E7-E5 in E6', wp.isValidMove(Position(self.game, 'E6')).valid)
        moves = wp.listValidMoves()
        print([str(x) for x in moves])
        wp.move_to('E6')
        self.game.chessBoard()
    def test_taking(self):
        wp = self.setup_test_1()
        wp.move_to('G6')
        self.game.chessBoard()
    def test_wrong_move(self):
        wp = self.setup_test_1()
        try:
            wp.move_to('E8')
            self.t_assert('Pawn E5 to E8 gives an exception', False)
        except:
            self.t_assert('Pawn E5 to E8 gives an exception', True)
    def test_cannot_take_vertically(self):
        self.game.empty_board()
        wp = self.game.place_piece(Pawn(self.game, Chess.WHITE), Position(self.game,'F4'))
        bp = self.game.place_piece(Pawn(self.game, Chess.BLACK), Position(self.game, 'F5'))
        self.game.chessBoard()
        self.t_assert('cannot take piece in front F4-F5', not wp.isValidMove(Position(self.game, 'F5')).valid)
    def test(self):
        self.test_starting()
        self.test_starting_black()
        self.test_is_valid_move()
        self.test_classic_moves()
        self.test_wrong_move()
        self.test_taking()
        self.test_back()
        self.test_no_jump()
        self.test_en_passant()
        self.test_cannot_take_vertically()
        self.test_cannot_take_vertically_after_double()