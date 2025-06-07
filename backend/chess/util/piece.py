from abc import ABC

from chess.color import ColorType


class ChessPiece(ABC):
   
    def __init__(self, type: ColorType) -> None:
        self.type = type
    
    def __str__(self) -> str:
        return self.__class__.__name__[0]
    
        
class King(ChessPiece):
    pass

class Queen(ChessPiece):
    pass

class Rook(ChessPiece):
    pass

class Bishop(ChessPiece):
    pass

class Knight(ChessPiece):
    def __str__(self) -> str:
        return 'N'

class Pawn(ChessPiece):
    pass


