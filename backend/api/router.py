from fastapi import APIRouter
from api.auth_router import router as auth_router
from api.game_router import router as game_router

router = APIRouter()
router.include_router(auth_router, tags=["Auth"], prefix="/auth")
router.include_router(game_router, tags=["Game"], prefix="/game")

