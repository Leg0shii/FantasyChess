from abc import ABC
from domain.enums.color import ColorType


class Piece(ABC):

    def __init__(self, type: ColorType) -> None:
        self.type = type

    def __str__(self) -> str:
        return self.__class__.__name__[0]
