class ChessPosition:

    def __init__(self, field: str) -> None:
        x = 'abcdefgh'.find(field[0])
        y = '87654321'.find(field[1])

        if x == -1 or y == -1:
            raise ValueError(f"Invalid chess position: {field}")

        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}{self.y}"
    
    def __repr__(self) -> str:
        return f"ChessPosition({self.x}, {self.y})"
    
class ChessMove:

    def __init__(self, start: ChessPosition, end: ChessPosition) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start} -> {self.end}"
    
    def __repr__(self) -> str:
        return f"ChessMove({self.start}, {self.end})"
    

class ChessMoveFactory:

    @staticmethod
    def parse_notation(notation: str) -> ChessMove:
        return ChessMove(
            ChessPosition(notation[0:2]), 
            ChessPosition(notation[2:4])
        )
    
    
