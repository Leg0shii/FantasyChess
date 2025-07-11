from fastapi import APIRouter

router = APIRouter()
router.include_router(router, tags=["Auth"], prefix="/auth")

@router.post("/register")
async def register(
    username: str,
    password: str,
) -> dict[str, str]:
    """Register a user."""
    return {"message": "Registered"}

@router.post("/login")
async def login(
    username: str,
    password: str,
) -> dict[str, str]:
    """Login a user."""
    return {"message": "Logged in"}

@router.post("/logout")
async def logout() -> dict[str, str]:
    """Logout a user."""
    return {"message": "Logged out"}
