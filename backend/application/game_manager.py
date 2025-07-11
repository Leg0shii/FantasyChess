from domain.chess.game import Game


class GameManager:
    def __init__(self) -> None:
        self.games = {}

    def add_game(self, game: Game) -> None:
        self.games[game.id] = game

    def get_game(self, game_id: str) -> Game:
        return self.games[game_id]
