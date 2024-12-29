from abc import ABC

from color import ColorType


class ChessPiece(ABC):
   
    abstract_movement = []
   
    def __init__(self, type: ColorType) -> None:
        self.type = type

    
    def __str__(self) -> str:
        return "".join(self.__class__.__name__[:1])