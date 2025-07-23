from domain.exceptions import GameNotFound
from domain.chess.game import Game


class GameManager:
    def __init__(self) -> None:
        self.games = {}

    def add_game(self, game: Game) -> None:
        self.games[game.id] = game

    def get_game(self, game_id: str) -> Game:
        game = self.games.get(game_id, None)
        if game is None:
            raise GameNotFound("Game could not be found")

        return game
