class Notation:

    def __init__(self, field: str) -> None:
        x = 'abcdefgh'.find(field[0])
        y = '87654321'.find(field[1])

        if x == -1 or y == -1:
            raise ValueError(f"Invalid chess position: {field}")

        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}{self.y}"
