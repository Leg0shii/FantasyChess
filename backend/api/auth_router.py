from fastapi import APIRouter
from api.models import RegisterRequest, LoginRequest, LogoutRequest

router = APIRouter()

@router.post("/register")
async def register(request: RegisterRequest) -> dict[str, str]:
    """Register a user."""
    return {"message": "Registered"}

@router.post("/login")
async def login(request: LoginRequest) -> dict[str, str]:
    """Login a user."""
    return {"message": "Logged in"}

@router.post("/logout")
async def logout(request: LogoutRequest) -> dict[str, str]:
    """Logout a user."""
    return {"message": "Logged out"}
