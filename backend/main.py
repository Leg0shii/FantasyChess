from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

from color import ColorType
from player import Player
from game import ChessGame

# uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

player_white = Player(ColorType.WHITE, 'Legoshi')
player_black = Player(ColorType.BLACK, 'Herr Prüß')
game = ChessGame(player_white, player_black)
