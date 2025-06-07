from fastapi import APIRouter
from api.auth_router import auth_router
from api.game_router import game_router

router = APIRouter()
router.include_router(auth_router, prefix="/auth")
router.include_router(game_router, prefix="/game")

