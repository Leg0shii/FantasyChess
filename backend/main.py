import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.router import router


frontend_url = os.getenv('FRONTEND_URL')

# uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
