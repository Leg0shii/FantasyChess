import type { Move, ChessPiece, PieceColor } from './chess.js';

export interface GameState {
    id: string;
    board: (ChessPiece | null)[][];
    currentPlayer: PieceColor;
    status: GameStatus;
    moves: Move[];
    players: {
      white: Player;
      black: Player;
    };
    createdAt: string;
    updatedAt: string;
}

export interface Player {
    name: string;
    rating?: number;
}

export type GameStatus = 'waiting' | 'active' | 'checkmate' | 'stalemate' | 'draw'