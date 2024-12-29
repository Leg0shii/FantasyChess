from color import ColorType
from piece.rook import Rook
from piece.knight import Knight
from piece.pawn import Pawn
from piece.bishop import Bishop
from piece.queen import Queen
from piece.king import King


class ChessBoard():

    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.init_start_position()

    
    def __str__(self) -> str:
        board_string = ''
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                piece = self.board[y][x]
                if piece:
                    if piece.type == ColorType.WHITE:
                        board_string += str(piece).upper()
                    else:
                        board_string += str(piece).lower()
                else:
                    board_string += "O"
            board_string += '\n'
        return board_string
    

    def init_start_position(self) -> None:
        self.set_pawns()
        self.set_rooks()
        self.set_knights()
        self.set_bishops()
        self.set_queens()
        self.set_kings()


    def set_pawns(self) -> None:
        for i in range(8):
            self.board[1][i] = Pawn(ColorType.BLACK)
            self.board[6][i] = Pawn(ColorType.WHITE)


    def set_rooks(self) -> None:
        self.board[0][0] = Rook(ColorType.BLACK)
        self.board[0][7] = Rook(ColorType.BLACK)
        self.board[7][0] = Rook(ColorType.WHITE)
        self.board[7][7] = Rook(ColorType.WHITE)

    
    def set_knights(self) -> None:
        self.board[0][1] = Knight(ColorType.BLACK)
        self.board[0][6] = Knight(ColorType.BLACK)
        self.board[7][1] = Knight(ColorType.WHITE)
        self.board[7][6] = Knight(ColorType.WHITE)

    
    def set_bishops(self) -> None:
        self.board[0][2] = Bishop(ColorType.BLACK)
        self.board[0][5] = Bishop(ColorType.BLACK)
        self.board[7][2] = Bishop(ColorType.WHITE)
        self.board[7][5] = Bishop(ColorType.WHITE)


    def set_queens(self) -> None:
        self.board[0][3] = Queen(ColorType.BLACK)
        self.board[7][3] = Queen(ColorType.WHITE)   

    
    def set_kings(self) -> None:
        self.board[0][4] = King(ColorType.BLACK)
        self.board[7][4] = King(ColorType.WHITE) 