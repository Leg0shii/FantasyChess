import logging
import uuid
from api.models.responses import GameStateResponse, GameStepResponse
from domain.exceptions import GameFull
from domain.models.player import Player
from domain.enums.game_state import GameStatus
from domain.enums.color import ColorType
from domain.models.move import Move, MoveFactory
from domain.chess.engine import Engine
from domain.chess.board import Board


class Game:

    def __init__(self, player_white, player_black=None) -> None:
        self.board = Board()
        self.engine = Engine(self.board)
        self.turn = ColorType.WHITE
        self.players = [player_white]

        if player_black:
            self.players.append(player_black)

        self.current_player = player_white
        self.history = []
        self.move_count = 0
        self.id = str(uuid.uuid4())

    def run_step(self, user_input: str) -> GameStepResponse:
        move = MoveFactory.parse_notation(user_input)
        if not self.is_move_allowed(move):
            raise ValueError(f"{user_input} is not a valid move.")

        self.apply_move(move)

        self.history.append(user_input)
        self.move_count += 1

        game_state = self.serialize()

        if self.has_won():
            return GameStepResponse(
                winner=self.current_player,
                state=GameStateResponse(
                    status=GameStatus.CHECKMATE,
                    game_state=game_state
                )
            )

        self.switch_state()
        return GameStepResponse(
            winner=None,
            state=GameStateResponse(
                status=GameStatus.IN_PROGRESS,
                game_state=game_state
            )
        )

    def add_player(self, player_name: str) -> None:
        if len(self.players) > 1:
            raise GameFull("The game is already full!")

        self.players.append(Player(name=player_name, color=ColorType.BLACK))

    def switch_state(self) -> None:
        if self.turn == ColorType.WHITE:
            self.turn = ColorType.BLACK
            self.current_player = self.players[1]
        else:
            self.turn = ColorType.WHITE
            self.current_player = self.players[0]

    def is_move_allowed(self, move: Move) -> bool:
        return self.engine.is_move_allowed(move)

    def has_won(self) -> bool:
        return self.engine.has_won()

    def apply_move(self, move: Move) -> None:
        logging.getLogger().debug(f"Applying move: {move}")
        field = self.board.board

        from_y = move.from_position.y
        from_x = move.from_position.x
        to_y = move.to_position.y
        to_x = move.to_position.x

        temp = field[from_y][from_x]
        field[from_y][from_x] = field[to_y][to_x]
        field[to_y][to_x] = temp

    def get_game_info(self) -> list[dict[str, str]]:
        return self.board.parse_ascii_chessboard()

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
