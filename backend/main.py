import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from api.routers import auth, game
from api.models.error import ErrorResponse
from domain.exceptions import DomainError

load_dotenv()

def create_app() -> FastAPI:
    """Factory function to create the FastAPI app"""
    frontend_url = os.getenv('FRONTEND_URL')
    if not frontend_url:
        raise ValueError("'FRONTEND_URL' is not initialized.")
    
    app = FastAPI(
        title="Fantasy Chess API",
        description="Chess game API",
        version="1.0.0"
    )
    
    # Exception handlers
    @app.exception_handler(DomainError)
    async def domain_error_handler(request: Request, exc: DomainError) -> JSONResponse:
        return JSONResponse(
            status_code=exc.status_code,
            content=ErrorResponse(code=exc.code, message=exc.message).model_dump(),
        )
    
    @app.exception_handler(Exception)
    async def unhandled_handler(request: Request, exc: Exception) -> JSONResponse:
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(
                code="internal-error",
                message="internal server error"
            ).model_dump(),
        )
    
    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            frontend_url, 
            "http://127.0.0.1:5173", 
            "http://localhost:5173", 
            "http://localhost", 
            "http://127.0.0.1"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Routers
    app.include_router(game.router, tags=["Game"], prefix="/game")
    app.include_router(auth.router, tags=["Auth"], prefix="/auth")
    
    return app

# Create app instance
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")