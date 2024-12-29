from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from color import ColorType
from player import Player
from game import ChessGame

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],  # Deine Frontend-URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

player_white = Player(ColorType.WHITE, 'Legoshi')
player_black = Player(ColorType.BLACK, 'Herr Prüß')
game = ChessGame(player_white, player_black)


@app.get("/api/positions")
def get_positions():
    return JSONResponse(content=game.get_game_info())
