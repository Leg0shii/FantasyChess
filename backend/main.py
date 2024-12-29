from color import ColorType
from player import Player
from game import ChessGame


def main() -> None:
    player_white = Player(ColorType.WHITE, 'Legoshi')
    player_black = Player(ColorType.BLACK, 'Herr Prüß')
    game = ChessGame(player_white, player_black)

    while not game.has_won():
        game.step()


if __name__ == "__main__":
    main()
