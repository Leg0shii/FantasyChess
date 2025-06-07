from fastapi import APIRouter, HTTPException
from api.models import CreateGameRequest, JoinGameRequest, LeaveGameRequest
from chess.util.color import ColorType
from chess.player.player import Player
from chess.game import ChessGame

router = APIRouter()
games = {}

@router.post("/game/create")
async def create_game(request: CreateGameRequest) -> dict[str, str]:
    """
    Create a new game session.
    """
    session_key = f"game-{len(games) + 1}"
    player_white = Player(ColorType.WHITE, request.player_name)
    game = ChessGame(player_white)
    games[session_key] = game
    return {"message": "Game created", "session_key": session_key}

@router.post("/game/join")
async def join_game(request: JoinGameRequest) -> dict[str, str]:
    """
    Join an existing game session.
    """
    session_key = request.session_key
    if session_key not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = games[session_key]
    if len(game.players) == 1:
        game.players.append(Player(ColorType.BLACK, request.player_name))
        return {"message": "Joined game", "session_key": session_key}
    else:
        raise HTTPException(status_code=400, detail="Game is already full")

@router.post("/game/leave")
async def leave_game(request: LeaveGameRequest) -> dict[str, str]:
    """
    Join an existing game session.
    """
    session_key = request.session_key
    if session_key not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = games[session_key]
    game.players = [p for p in game.players if p.name != request.player_name]
    return {"message": "Left game", "session_key": session_key}

@router.get("/game/state")
async def get_game_state(session_key: str):
    """
    Get the current game state for a session.
    """
    if session_key not in games:
        raise HTTPException(status_code=404, detail="Game not found")

    game = games[session_key]
    return {"message": "Game state retrieved", "game_state": game.serialize()} 

@router.post("/game/step")
async def game_step(session_key: str, move: str):
    """
    Run one step of the game by applying the player's move.

    Args:
        session_key (str): The session key of the game.
        move (str): The player's move in algebraic notation.

    Returns:
        dict: The updated game state.
    """
    if session_key not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game = games[session_key]
    try:
        result = game.run_step(move)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
