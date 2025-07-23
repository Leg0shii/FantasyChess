from application.game_manager import GameManager
from application.player_manager import PlayerManager

game_manager = GameManager()
player_manager = PlayerManager()


def get_game_manager() -> GameManager:
    return game_manager


def get_player_manager() -> PlayerManager:
    return player_manager
