from chess.position import ChessMove
from chess.board import ChessBoard


class ChessEngine:

    def __init__(self, board: ChessBoard) -> None:
        self.board = board
    

    def is_move_allowed(self, move: ChessMove) -> bool:
        piece_to_move = None
        return True


    def has_won(self) -> None:
        return False
