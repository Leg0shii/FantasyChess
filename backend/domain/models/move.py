from dataclasses import dataclass

from domain.chess.moves.notation import Notation


@dataclass
class Move:
    from_position: Notation
    to_position: Notation


class MoveFactory:

    @staticmethod
    def parse_notation(notation: str) -> Move:
        return Move(
            from_position=Notation(notation[0:2]), 
            to_position=Notation(notation[2:4])
        )
