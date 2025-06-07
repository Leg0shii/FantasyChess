import uuid
from fastapi import logger
from chess.util.position import ChessMove, ChessMoveFactory
from engine.engine import ChessEngine
from chess.util.color import ColorType
from chess.board import ChessBoard


class ChessGame:

    def __init__(self, player_white, player_black=None) -> None:
        self.chess_board = ChessBoard()
        self.engine = ChessEngine(self.chess_board)
        self.turn = ColorType.WHITE
        self.players = [player_white]

        if player_black:
            self.players.append(player_black)

        self.current_player = player_white
        self.history = []
        self.move_count = 0
        self.id = str(uuid.uuid4())
    

    def run_step(self, user_input: str) -> None:
        move = ChessMoveFactory.parse_notation(user_input)
        if not self.is_move_allowed(move):
            raise ValueError(f"{user_input} is not a valid move.")

        self.apply_move(move)

        self.history.append(user_input)
        self.move_count += 1

        if self.has_won():
            return {
                "status": "game_over",
                "winner": self.current_player.name,
                "game_state": self.serialize()
            }

        self.switch_state()
        return {
            "status": "in_progress",
            "game_state": self.serialize()
        }


    def switch_state(self) -> None:
        if self.turn == ColorType.WHITE:
            self.turn = ColorType.BLACK
            self.current_player = self.players[1]
        else:
            self.turn = ColorType.WHITE
            self.current_player = self.players[0]

    
    def is_move_allowed(self, move: ChessMove) -> bool:
        return self.engine.is_move_allowed(move)


    def has_won(self) -> None:
        return self.engine.has_won()
    

    def apply_move(self, move: ChessMove) -> None:
        logger.debug(f"Applying move: {move}")
        field = self.chess_board.board

        temp = field[move.start.y][move.start.x]
        field[move.start.y][move.start.x] = field[move.end.y][move.end.x]
        field[move.end.y][move.end.x] = temp

    
    def get_game_info(self) -> str:
        return self.chess_board.parse_ascii_chessboard()
    

    def serialize(self) -> dict:
        """
        Serialize the game state into a JSON-serializable dictionary.
        """
        return {
            "chess_board": self.get_game_info(),
            "turn": self.turn.value,
            "players": [
                {
                    "name": player.name,
                    "color": player.color.value
                } for player in self.players if player is not None
            ],
            "current_player": {
                "name": self.current_player.name,
                "color": self.current_player.color.value
            },
            "history": self.history,
            "move_count": self.move_count
        }