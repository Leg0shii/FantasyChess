from typing import Any
from pydantic import BaseModel

from domain.enums.game_state import GameStatus
from domain.models.player import Player


class CreateGameResponse(BaseModel):
    message: str
    session_key: str

class JoinGameResponse(BaseModel):
    message: str
    session_key: str

class LeaveGameResponse(BaseModel):
    message: str
    session_key: str

class GameStepResponse(BaseModel):
    winner: Player | None = None
    status: GameStatus
    game_state: dict[str, Any]