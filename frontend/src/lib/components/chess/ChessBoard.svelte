<script lang="ts">
    import { currentGame, gameLoading } from "$lib/stores/game.js";
    import { chessAPI } from "$lib/services/chess-api.js";
    import ChessSquare from "./ChessSquare.svelte";
    import type { Position } from "$lib/types/chess.js";

    export let gameId: string;

    let selectedSquare: Position | null = null;

    async function handleSquareClick(row: number, col: number): Promise<void> {
        if ($gameLoading) return;

        if (selectedSquare) {
            try {
                await chessAPI.makeMove(gameId, {
                    from: selectedSquare,
                    to: { row, col },
                });
                selectedSquare = null;
            } catch (error) {
                console.error("Invalid move:", error);
                selectedSquare = null;
            }
        } else {
            selectedSquare = { row, col };
        }
    }

    function isSquareSelected(row: number, col: number): boolean {
        return selectedSquare?.row === row && selectedSquare?.col === col;
    }
</script>

{#if $gameLoading}
    <div class="loading">Loading game...</div>
{:else if $currentGame}
    <div class="chess-board">
        {#each $currentGame.board as row, i}
            {#each row as piece, j}
                <ChessSquare
                    {piece}
                    position={{ row: i, col: j }}
                    selected={isSquareSelected(i, j)}
                    onclick={(pos) => handleSquareClick(pos.row, pos.col)}
                />
            {/each}
        {/each}
    </div>
{/if}

<style>
	.chess-board {
		display: grid;
		grid-template-columns: repeat(8, var(--square, 60px));
		grid-auto-rows: var(--square, 60px);
	}
</style>
