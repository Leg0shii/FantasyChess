import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import auth, game

load_dotenv()

frontend_url = os.getenv('FRONTEND_URL')
if not frontend_url:
    raise ValueError("'FRONTEND_URL' is not initialized.")

# uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(game.router)
