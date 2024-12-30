from board import ChessBoard


class ChessEngine:

    def __init__(self, board: ChessBoard) -> None:
        self.board = board
    

    def is_move_allowed(self, user_input: list) -> bool:
        if user_input is None:
            return False
        
        piece_to_move = None
        return True


    def has_won(self) -> None:
        return False
