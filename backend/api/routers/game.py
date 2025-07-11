from fastapi import APIRouter, Depends, HTTPException
from domain.chess.game import Game
from domain.enums.color import ColorType
from domain.models.player import Player
from application.game_manager import GameManager
from application.player_manager import PlayerManager
from api.dependencies import get_game_manager, get_player_manager
from api.models.responses import CreateGameResponse, JoinGameResponse, LeaveGameResponse, GameStepResponse

router = APIRouter()
router.include_router(router, tags=["Game"], prefix="/game")

@router.post("/create")
async def create_game(
    player_name: str,
    player_manager: PlayerManager=Depends(get_player_manager),
    game_manager: GameManager=Depends(get_game_manager),
) -> CreateGameResponse:
    """Create a new game session."""
    player_white = Player(name=player_name, color=ColorType.WHITE)
    player_manager.add_player(player_white)

    game = Game(player_white)
    game_manager.add_game(game)

    return CreateGameResponse(message="Game created", session_key=game.id)

@router.post("/join")
async def join_game(
    session_key: str,
    player_name: str,
    game_manager: GameManager=Depends(get_game_manager),
) -> JoinGameResponse:
    """Join an existing game session."""
    game = game_manager.get_game(session_key)
    if len(game.players) == 1:
        game.players.append(Player(name=player_name, color=ColorType.BLACK))
        return JoinGameResponse(message="Joined game", session_key=game.id)
    else:
        raise HTTPException(status_code=400, detail="Game is already full")

@router.post("/leave")
async def leave_game(
    session_key: str,
    player_name: str,
    game_manager: GameManager=Depends(get_game_manager),
) -> LeaveGameResponse:
    """Join an existing game session."""
    game = game_manager.get_game(session_key)
    game.players = [p for p in game.players if p.name != player_name]
    return LeaveGameResponse(message="Left game", session_key=game.id)

@router.post("/step")
async def game_step(
    session_key: str,
    move: str,
    game_manager: GameManager=Depends(get_game_manager),
) -> GameStepResponse:
    """Run one step of the game by applying the player's move."""
    game = game_manager.get_game(session_key)
    try:
        return game.run_step(move)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
