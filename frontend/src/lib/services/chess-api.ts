import type { CreateGameRequest, CreateGameResponse } from "$lib/types/api";
import type { BoardMatrix, ChessPiece, Move, PieceColor, PieceType, Position } from "$lib/types/chess";

const API_BASE = 'http://localhost:8000';

function toChessPiece(obj: any): ChessPiece {
	// obj.type & obj.color are plain strings → cast to the union types
	return {
		type: obj.type as PieceType,
		color: obj.color as PieceColor
	};
}

function pieceListToMatrix(list: any[]): BoardMatrix {
	const emptyRow = () => Array<ChessPiece | null>(8).fill(null);
	const board: BoardMatrix = Array.from({ length: 8 }, emptyRow);

	for (const obj of list) {
		// "a8" → file = 'a', rank = 8
		const file = obj.square[0];
		const rank = Number(obj.square[1]);   // 1–8

		const col = file.charCodeAt(0) - 'a'.charCodeAt(0); // 0–7
		const row = 8 - rank;                               // 0–7  (Rank-8 oben)

		board[row][col] = {
			type: obj.piece as PieceType,
			color: obj.color as PieceColor
		};
	}
	return board;
}

export class ChessAPIService {
    async createGame(request: CreateGameRequest): Promise<CreateGameResponse> {
        const response = await fetch(`${API_BASE}/game/create`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ player_name: request.player.name })
        });
        if (!response.ok) throw new Error('Failed to create game');
        return response.json();
    }

    async getGame(gameId: string): Promise<any> {
        const response = await fetch(`${API_BASE}/game/${gameId}`);
        if (!response.ok) throw new Error('Failed to fetch game');

        const { status, game_state } = await response.json();
        const board = pieceListToMatrix(game_state.chess_board);
        
        return { gameId, status, board, ...game_state };
    }

    async makeMove(gameId: string, move: Move): Promise<any> {
        const response = await fetch(`${API_BASE}/games/${gameId}/moves`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(move)
        });
        if (!response.ok) throw new Error('Invalid move');
        return response.json();
    }
}

export const chessAPI: ChessAPIService = new ChessAPIService();