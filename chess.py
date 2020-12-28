from piece import Piece
from position import Position


class Game:
    def start(self):
        self.init_board()
        print ("game started")
    def end(self):
        print ("game ended")

class Chess(Game):
    """ The main Chess game representation """
    cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    rows= ['1', '2', '3', '4', '5', '6', '7', '8']
    BLACK = 'Black'
    WHITE = 'White'
    board = {}
    WHITE_KING = '\u2654'
    WHITE_QUEEN = '\u2655'
    WHITE_ROOK = '\u2656'
    WHITE_BISHOP = '\u2657'
    WHITE_KNIGHT = '\u2658'
    WHITE_PAWN= '\u2659'
    BLACK_KING = '\u265A'
    BLACK_QUEEN = '\u265B'
    BLACK_ROOK = '\u265C'
    BLACK_BISHOP = '\u265D'
    BLACK_KNIGHT ='\u265E'
    BLACK_PAWN = '\u265F'
    representation = {
        'King' : {
            BLACK : BLACK_KING,
            WHITE : WHITE_KING
        },
        'Queen': {
            BLACK : BLACK_QUEEN,
            WHITE : WHITE_QUEEN
        },
        'Rook': {
            BLACK : BLACK_ROOK,
            WHITE : WHITE_ROOK
        },
        'Bishop': {
            BLACK : BLACK_BISHOP,
            WHITE : WHITE_BISHOP
        },
        'Knight': {
            BLACK : BLACK_KNIGHT,
            WHITE : WHITE_KNIGHT
        },
        'Pawn': {
            BLACK : BLACK_PAWN,
            WHITE : WHITE_PAWN
        }
    }
    def place_piece(self, piece, position):
        self.remove(piece)
        return self.add_piece(piece, position)
    def add_piece(self, piece, position):
        if type(position).__name__ != 'Position':
            raise Exception(f"Invalid Position '{position}'")
        if type(piece).__base__.__name__ != 'Piece':
            raise Exception(f"Invalid Piece '{piece}'")
        piece.setPosition(position) #tell the piece its position
        print(f'placing a {piece} in {str(position)}')
        self.board[str(position)] = piece # tell the board what is in that position
        #self.chessBoard()
        return piece #updated piece
    def empty_board(self):
        self.board = {}
        self.move_count = 0
        self.last_move = None #(piece, old_position)
        self.next_to_move = self.WHITE
    def init_board(self):
        from pawn import Pawn
        from king import King
        from queen import Queen
        from knight import Knight
        from bishop import Bishop
        from rook import Rook
        self.empty_board()
        self.board['A2'] =  Pawn(self, self.WHITE, Position(self,'A2'))
        self.board['B2'] =  Pawn(self, self.WHITE, Position(self,'B2'))
        self.board['C2']=  Pawn(self, self.WHITE, Position(self,'C2'))
        self.board['D2'] =  Pawn(self, self.WHITE, Position(self,'D2'))
        self.board['E2'] =  Pawn(self, self.WHITE, Position(self,'E2'))
        self.board['F2']=  Pawn(self, self.WHITE, Position(self,'F2'))
        self.board['G2'] =  Pawn(self, self.WHITE, Position(self,'G2'))
        self.board['H2']=  Pawn(self, self.WHITE, Position(self,'H2'))
        self.board['A7'] =  Pawn(self, self.BLACK, Position(self,'A7'))
        self.board['B7'] =  Pawn(self, self.BLACK, Position(self,'B7'))
        self.board['C7'] =  Pawn(self, self.BLACK, Position(self,'C7'))
        self.board['D7'] =  Pawn(self, self.BLACK, Position(self,'D7'))
        self.board['E7'] =  Pawn(self, self.BLACK, Position(self,'E7'))
        self.board['F7']=  Pawn(self, self.BLACK, Position(self,'F7'))
        self.board['G7'] =  Pawn(self, self.BLACK, Position(self,'G7'))
        self.board['H7']=  Pawn(self, self.BLACK, Position(self,'H7'))
        self.board['A1'] =  Rook(self, self.WHITE, Position(self,'A1'))
        self.board['B1'] =  Knight(self, self.WHITE, Position(self,'B1'))
        self.board['C1']=  Bishop(self, self.WHITE, Position(self,'C1'))
        self.board['D1'] =  Queen(self, self.WHITE, Position(self,'D1'))
        self.board['E1'] =  King(self, self.WHITE, Position(self,'E1'))
        self.board['F1']=  Bishop(self, self.WHITE, Position(self,'F1'))
        self.board['G1'] =  Knight(self, self.WHITE, Position(self,'G1'))
        self.board['H1']=  Rook(self, self.WHITE, Position(self,'H1'))
        self.board['A8'] =  Rook(self, self.BLACK, Position(self,'A8'))
        self.board['B8'] =  Knight(self, self.BLACK, Position(self,'B8'))
        self.board['C8']=  Bishop(self, self.BLACK, Position(self,'C8'))
        self.board['D8'] =  Queen(self, self.BLACK, Position(self,'D8'))
        self.board['E8'] =  King(self, self.BLACK, Position(self,'E8'))
        self.board['F8']=  Bishop(self, self.BLACK, Position(self,'F8'))
        self.board['G8'] =  Knight(self, self.BLACK, Position(self,'G8'))
        self.board['H8']=  Rook(self, self.BLACK, Position(self,'H8'))

    def move_to(self, piece, A1Str, opponent):
        return self.move(piece, Position(self, A1Str), opponent)

    def remove(self, piece):
        if piece != None :
            if piece.position != None : 
                self.board[str(piece.position)] = None # remove the piece from original position
                piece.detachPosition() #piece.position = None

    def move(self, piece, position, opponent, effect):
        if piece.color != self.next_to_move:
            raise Exception(f'wrong turn, on move {self.move_count + 1}, it should be {self.next_to_move}, seeing {str(piece)} instead')
        self.move_count += 1
        if self.next_to_move == self.BLACK: self.next_to_move = self.WHITE
        else: self.next_to_move = self.BLACK
        self.last_move = (piece, piece.position) #piece.position will be modified by place_piece
        #TODO  : register position on board, possibly remove occupying piece
        self.place_piece(piece, position)
        if effect != None : effect()
        self.chessBoard()

    def occupation(self, position):
        try:
            piece = self.board[str(position)]
        except KeyError:
            piece = None
        return piece
    def getBlacks(self, position):
        pass
    def squareDoesExist(self, col, row):
        return row in self.rows and col in self.cols
    
    def displaySquareOccupation(self, col, row):
        piece = self.occupation(Position.strings2A1Str(col, row)) #Position(self, Position.strings2A1Str(col, row)))
        if piece == None: return "."
        else : return str(piece) #self.representation[piece.name][piece.color]
        
    def chessBoardRow(self, row):
        print('{0} || {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8}'.format(
            row,
            self.displaySquareOccupation('A', row).center(4,' '),
            self.displaySquareOccupation('B', row).center(4, ' '),
            self.displaySquareOccupation('C', row).center(4, ' '),
            self.displaySquareOccupation('D', row).center(4, ' '),
            self.displaySquareOccupation('E', row).center(4, ' '),
            self.displaySquareOccupation('F', row).center(4, ' '),
            self.displaySquareOccupation('G', row).center(4, ' '),
            self.displaySquareOccupation('H', row).center(4, ' ')

            ))
        print('__||______|______|______|______|______|______|______|______|')
    def chessBoard(self):
        for i in range (1, 9):
            self.chessBoardRow(str(9 - i))
        print('--||------|------|------|------|------|------|------|------|')
        print('  ||   A  |   B  |   C  |   D  |   E  |   F  |   G  |   H  |')

class Moves:
    pass

