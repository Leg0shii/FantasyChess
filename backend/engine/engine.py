from domain.models.move import Move
from chess.board import Board


class Engine:

    def __init__(self, board: Board) -> None:
        self.board = board
    

    def is_move_allowed(self, move: Move) -> bool:
        return True


    def has_won(self) -> bool:
        return False
