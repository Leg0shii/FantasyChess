from typing import Any
from pydantic import BaseModel

class CreateGameResponse(BaseModel):
    message: str
    session_key: str

class JoinGameResponse(BaseModel):
    message: str
    session_key: str

class LeaveGameResponse(BaseModel):
    message: str
    session_key: str

class GameStateResponse(BaseModel):
    message: str
    game_state: dict[str, Any]

class GameStepResponse(BaseModel):
    message: str
    game_state: dict[str, Any]