<script lang="ts">
    import { onMount } from "svelte";
    import { page } from "$app/stores";
    import { currentGame, gameLoading } from "$lib/stores/game.js";
    import { chessAPI } from "$lib/services/chess-api.js";
    import ChessBoard from "$lib/components/chess/ChessBoard.svelte";
    import GameStatus from "$lib/components/chess/GameStatus.svelte";

    $: gameId = $page.params.id;

    onMount(async () => {
        const game = await chessAPI.getGame(gameId);
        gameLoading.set(false);
        currentGame.set(game);
    });
</script>

<svelte:head>
    <title>Chess Game {gameId}</title>
</svelte:head>

<div class="game-container">
    <div class="game-board">
        <ChessBoard {gameId} />
    </div>

    <div class="game-info">
        <GameStatus />
    </div>
</div>

<style>
    .game-container {
        display: flex;
        gap: 2rem;
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
</style>
