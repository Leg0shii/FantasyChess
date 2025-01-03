from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

# uvicorn main:app --reload 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://127.0.0.1:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
