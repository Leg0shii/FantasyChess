from dataclasses import dataclass
import uuid
from domain.enums.color import ColorType


@dataclass
class Player:
    name: str
    color: ColorType 

    def __post_init__(self) -> None:
        self.id = str(uuid.uuid4())