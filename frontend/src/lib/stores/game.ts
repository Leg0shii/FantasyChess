import type { BoardMatrix } from '$lib/types/chess';
import { writable, derived, type Writable, type Readable } from 'svelte/store';

export const currentGame = writable<
	| {
			id: string;
			status: string;
			board: BoardMatrix;
	  }
	| null
>(null);
export const gameLoading: Writable<boolean> = writable(false);
export const gameError: Writable<any> = writable(null);

export const isPlayerTurn: Readable<boolean> = derived(
  currentGame,
  $game => $game?.currentPlayer === 'white' // or based on actual player
);

export const gameStatus: Readable<any> = derived(
  currentGame,
  $game => $game?.status || 'waiting'
);