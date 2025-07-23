<script lang="ts">
    import type { Position, ChessPiece } from "$lib/types/chess.js";

    interface Props {
        piece: ChessPiece | null;
        position: Position;
        selected?: boolean;
        onclick?: (position: Position) => void;
    }

    let { piece, position, selected = false, onclick }: Props = $props();

    function handleClick(): void {
        onclick?.(position);
    }

    // Determine square color based on position
    let isLightSquare = $derived((position.row + position.col) % 2 === 0);
</script>

<button
    class="chess-square"
    class:light={isLightSquare}
    class:dark={!isLightSquare}
    class:selected
    class:has-piece={!!piece}
    onclick={handleClick}
    aria-label="Square {String.fromCharCode(97 + position.col)}{8 -
        position.row}"
>
    {#if piece}
        <div
            class="piece {piece.type} {piece.color}"
            aria-label="{piece.color} {piece.type}"
        ></div>
    {/if}
</button>

<style>
    .chess-square {
        width: 60px;
        height: 60px;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        position: relative;
        transition: all 0.2s ease;
        font-size: 0;
    }

    .chess-square:hover {
        filter: brightness(1.1);
    }

    .chess-square:focus {
        outline: 2px solid #007acc;
        outline-offset: -2px;
    }

    .light {
        background-color: #f0d9b5;
    }

    .dark {
        background-color: #b58863;
    }

    .selected {
        background-color: #ffff99 !important;
        box-shadow: inset 0 0 0 3px #ffcc00;
    }

    .has-piece:hover {
        background-color: rgba(255, 255, 0, 0.3);
    }

    .piece {
        width: 80%;
        height: 80%;
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        pointer-events: none;
    }

    /* Optional: Add hover effect for valid moves */
    .chess-square.valid-move {
        background-color: rgba(0, 255, 0, 0.3);
    }

    .chess-square.valid-move::after {
        content: "";
        position: absolute;
        width: 20px;
        height: 20px;
        background-color: rgba(0, 255, 0, 0.6);
        border-radius: 50%;
    }
</style>
