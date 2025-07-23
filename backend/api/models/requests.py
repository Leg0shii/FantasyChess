from pydantic import BaseModel


class CreateGameRequest(BaseModel):
    player_name: str


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str