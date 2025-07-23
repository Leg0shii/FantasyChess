export interface Position {
    row: number;
    col: number;
}

export interface Square {
    position: Position
    piece: ChessPiece | null;
}

export interface ChessPiece {
    type: PieceType,
    color: PieceColor,
}

export interface Move {
    from: Position;
    to: Position;
}

export interface ChessMove {
    move: Move;
    piece: ChessPiece;
    capturedPiece?: ChessPiece;
    notation?: string;
    timestamp?: string;
}

export type PieceType = 'pawn' | 'rook' | 'knight' | 'bishop' | 'queen' | 'king';
export type PieceColor = 'white' | 'black';

export type BoardMatrix = (ChessPiece | null)[][];
