from fastapi import APIRouter

from api.models.requests import RegisterRequest, LoginRequest
from api.models.responses import InformationResponse

router = APIRouter()


@router.post("/register")
async def register(request: RegisterRequest) -> InformationResponse:
    """Register a user."""
    return InformationResponse(message="Registered.")


@router.post("/login")
async def login(request: LoginRequest) -> InformationResponse:
    """Login a user."""
    return InformationResponse(message="Logged in")


@router.post("/logout")
async def logout() -> InformationResponse:
    """Logout a user."""
    return InformationResponse(message="Logged out")
