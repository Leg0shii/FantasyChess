from fastapi import APIRouter, Depends, HTTPException
from chess.game_manager import GameManager
from chess.player.player_manager import PlayerManager
from chess.util.color import ColorType
from chess.player.player import Player
from chess.game import ChessGame
from dependencies import get_game_manager, get_player_manager
from api.models import CreateGameResponse, JoinGameResponse, LeaveGameResponse, GameStateResponse, GameStepResponse

router = APIRouter()

@router.post("/create")
async def create_game(
    player_name: str,
    player_manager: PlayerManager=Depends(get_player_manager),
    game_manager: GameManager=Depends(get_game_manager),
) -> CreateGameResponse:
    """Create a new game session."""
    player_white = Player(ColorType.WHITE, player_name)
    player_manager.add_player(player_white)

    game = ChessGame(player_white)
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
        game.players.append(Player(ColorType.BLACK, player_name))
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

@router.get("/state")
async def get_game_state(
    session_key: str,
    game_manager: GameManager=Depends(get_game_manager),
) -> GameStateResponse:
    """Get the current game state for a session."""
    game = game_manager.get_game(session_key)
    return GameStateResponse(message="Game state retrieved", game_state=game.serialize()) 

@router.post("/step")
async def game_step(
    session_key: str,
    move: str,
    game_manager: GameManager=Depends(get_game_manager),
) -> GameStepResponse:
    """Run one step of the game by applying the player's move."""
    game = game_manager.get_game(session_key)
    try:
        result = game.run_step(move)
        return GameStepResponse(message="Game step executed", game_state=game.serialize())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
