from utils import Object

class Position:
    def __str__(self):
        return f'{self.col}{self.row}'
    @staticmethod
    def num2col(numCol):
        return chr(ord('A') + numCol - 1)
    @staticmethod
    def num2row(numRow):
        return str(numRow)
    @staticmethod
    def col2num(col):
        return ord(col) - ord('A') + 1
    @staticmethod
    def row2num(row):
        return int(row)
    @staticmethod
    def nums2A1Str(colNum,rowNum):
        return f'{Position.num2col(colNum)}{Position.num2row(rowNum)}'
    @staticmethod
    def strings2A1Str(col,row):
        return f'{col}{row}'
    @staticmethod
    def left_square(position):
        colNum = position.colNum - 1
        row = position.row
        if colNum >= 1 : return Position(position.game,f'{Position.num2col(colNum)}{row}')
        return None
    
    @staticmethod
    def right_square(position):
        colNum = position.colNum + 1
        row = position.row
        if colNum <= 8 : return Position(position.game,f'{Position.num2col(colNum)}{row}')
        return None
    @staticmethod
    def upleft_square(position):
        colNum = position.colNum - 1
        rowNum = position.rowNum + 1
        if colNum >= 1 and rowNum <= 8 : return Position(position.game,f'{Position.num2col(colNum)}{Position.num2col(rowNum)}')
        return None

    @staticmethod
    def upright_square(position):
        colNum = position.colNum + 1
        rowNum = position.rowNum + 1
        if colNum <= 8 and rowNum <= 8 : return Position(position.game,f'{Position.num2col(colNum)}{Position.num2col(rowNum)}')
        return None
    @staticmethod
    def up_square(position):
        rowNum = position.rowNum + 1
        col = position.col
        if rowNum <= 8 : return Position(position.game,f'{col}{Position.num2col(rowNum)}')
        return None
    @staticmethod
    def down_square(position):
        rowNum = position.rowNum - 1
        col = position.col
        if rowNum >= 1 : return Position(position.game,f'{col}{Position.num2col(rowNum)}')
        return None
    @staticmethod
    def downleft_square(position):
        colNum = position.colNum - 1
        rowNum = position.rowNum - 1
        if colNum >= 1 and rowNum >= 1 : return Position(position.game,f'{Position.num2col(colNum)}{Position.num2col(rowNum)}')
        return None

    @staticmethod
    def downright_square(position):
        colNum = position.colNum + 1
        rowNum = position.rowNum - 1
        if colNum <= 8 and rowNum >= 1: return Position(position.game,f'{Position.num2col(colNum)}{Position.num2col(rowNum)}')
        return None

    @staticmethod
    def movesMaxMins(position):
        up_delta_row = 8 - position.rowNum
        down_delta_row = 1 - position.rowNum 
        right_delta_col = 8 - position.colNum
        left_delta_col = 1 - position.colNum   
        upright_delta_diag = min(right_delta_col, up_delta_row)
        downleft_delta_diag = -min(abs(left_delta_col), abs(down_delta_row))
        downright_delta_diag = min(right_delta_col, abs(down_delta_row))
        upleft_delta_diag = -min(abs(left_delta_col), up_delta_row)
        return Object(
            up_delta_row = up_delta_row,
            down_delta_row =  down_delta_row,
            right_delta_col =  right_delta_col,
            left_delta_col =  left_delta_col,
            downleft_delta_diag = downleft_delta_diag,
            upright_delta_diag = upright_delta_diag,
            downright_delta_diag = downright_delta_diag,
            upleft_delta_diag = upleft_delta_diag
        )
    def __init__(self,game, A1Str):
        col = A1Str[0]
        row = A1Str[1]
        if not game.squareDoesExist(col, row):
            raise Exception(f"Invalid Position '{col}{row}'")
        self.row = row
        self.col = col
        self.rowNum = int(row)
        self.colNum = Position.col2num(col) 
