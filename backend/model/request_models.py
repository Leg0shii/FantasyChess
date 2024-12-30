from pydantic import BaseModel

class CreateGameRequest(BaseModel):
    player_name: str


class JoinGameRequest(BaseModel):
    session_key: str
    player_name: str


class LeaveGameRequest(BaseModel):
    session_key: str
    player_name: str