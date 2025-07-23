from fastapi import APIRouter, Body, Depends
from api.models.requests import CreateGameRequest
from domain.enums.game_state import GameStatus
from domain.chess.game import Game
from domain.enums.color import ColorType
from domain.models.player import Player
from application.game_manager import GameManager
from application.player_manager import PlayerManager
from api.dependencies import get_game_manager, get_player_manager
from api.models.responses import (
    CreateGameResponse,
    GameStateResponse,
    JoinGameResponse,
    LeaveGameResponse,
    GameStepResponse,
)

router = APIRouter()


@router.post("/create")
async def create_game(
    request: CreateGameRequest = Body(...),
    player_manager: PlayerManager = Depends(get_player_manager),
    game_manager: GameManager = Depends(get_game_manager),
) -> CreateGameResponse:
    """Create a new game session."""
    player_white = Player(name=request.player_name, color=ColorType.WHITE)
    player_manager.add_player(player_white)

    game = Game(player_white)
    game_manager.add_game(game)

    return CreateGameResponse(message="Game created", session_key=game.id)


@router.get("/{session_key}")
async def get_game_state(session_key: str) -> GameStateResponse:
    """Get the current game state for a session."""
    game = get_game_manager().get_game(session_key)
    return GameStateResponse(
        status=GameStatus.IN_PROGRESS,
        game_state=game.serialize()
    )


@router.post("/join")
async def join_game(
    session_key: str,
    player_name: str,
    game_manager: GameManager = Depends(get_game_manager),
) -> JoinGameResponse:
    """Join an existing game session."""
    game = game_manager.get_game(session_key)
    game.add_player(player_name)
    return JoinGameResponse(message="joined", session_key=game.id)


@router.post("/leave")
async def leave_game(
    session_key: str,
    player_name: str,
    game_manager: GameManager = Depends(get_game_manager),
) -> LeaveGameResponse:
    """Join an existing game session."""
    game = game_manager.get_game(session_key)
    game.players = [p for p in game.players if p.name != player_name]
    return LeaveGameResponse(message="Left game", session_key=game.id)


@router.post("/step")
async def game_step(
    session_key: str,
    move: str,
    game_manager: GameManager = Depends(get_game_manager),
) -> GameStepResponse:
    """Run one step of the game by applying the player's move."""
    game = game_manager.get_game(session_key)
    return game.run_step(move)
