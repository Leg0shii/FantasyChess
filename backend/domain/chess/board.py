from domain.chess.pieces.base import Piece
from domain.enums.color import ColorType
from domain.chess.pieces.rook import Rook
from domain.chess.pieces.knight import Knight
from domain.chess.pieces.bishop import Bishop
from domain.chess.pieces.queen import Queen
from domain.chess.pieces.king import King
from domain.chess.pieces.pawn import Pawn


class Board():

    def __init__(self) -> None:
        self.board: list[list[Piece | None]] = [[None for _ in range(8)] for _ in range(8)]
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
    

    def parse_ascii_chessboard(self) -> list[dict[str, str]]:
        piece_map = {
            'r': 'rook',
            'n': 'knight',
            'b': 'bishop',
            'q': 'queen',
            'k': 'king',
            'p': 'pawn'
        }

        ascii_board = str(self)
        lines = ascii_board.strip().split('\n')
        result = []

        for row, line in enumerate(lines):
            rank = 8 - row
            for col, char in enumerate(line):
                if char != 'O':
                    color = "white" if char.isupper() else "black"
                    piece_type = piece_map[char.lower()]
                    square = f"{chr(ord('a') + col)}{rank}"
                    result.append({"square": square, "piece": piece_type, "color": color})

        return result
    

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