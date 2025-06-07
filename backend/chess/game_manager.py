from chess.game import ChessGame


class GameManager:
    def __init__(self) -> None:
        self.games = {}

    def add_game(self, game: ChessGame) -> None:
        self.games[game.id] = game

    def get_game(self, game_id: str) -> ChessGame:
        return self.games[game_id]
