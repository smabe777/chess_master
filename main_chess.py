from chess import Chess
from position import Position

if __name__ == '__main__':
    from test_pawn import Test_Pawn
    from test_king import Test_King
    from test_queen import Test_Queen
    game = Chess()
    game.start()
    print(game.occupation(Position(game, 'H4')))
    game.chessBoard()
    #Test_King(game).result()
    Test_Queen(game).result()
    #Test_Pawn(game).result()
