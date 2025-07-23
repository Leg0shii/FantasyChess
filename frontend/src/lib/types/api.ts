import type { Move, Position } from './chess.js';
import type { GameState, Player } from './game.js';

export interface CreateGameRequest {
  player: Player;
}

export interface MakeMoveRequest {
  from: Position;
  to: Position;
}

export interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

export interface CreateGameResponse {
  message: string;
  session_key: string;
}

export type GameResponse = APIResponse<GameState>;
export type MoveResponse = APIResponse<{ game: GameState; move: Move }>;