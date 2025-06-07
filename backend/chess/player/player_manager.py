from chess.player.player import Player


class PlayerManager:

    def __init__(self) -> None:
        self.players = {}

    def add_player(self, player: Player) -> None:
        self.players[player.id] = player

    def remove_player(self, player_id: str) -> None:
        del self.players[player_id]

    def get_player(self, player_id: str) -> Player:
        return self.players[player_id]
