from chess.color import ColorType


class Player:

    def __init__(self, color: ColorType, name: str) -> None:
        self.color = color
        self.name = name
        