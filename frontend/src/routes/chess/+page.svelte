<script lang="ts">
    import { goto } from "$app/navigation";
	import { chessAPI } from "$lib/services/chess-api.js";

    let playerId = "1";
    let playerName = 'Test Name';
    let playerRating = 0;

    async function handleCreateGame() {
		const data = await chessAPI.createGame({
            player: {
                id: playerId,
                name: playerName,
                rating: playerRating
            }
        });

        const sessionKey = data.session_key;
        goto("/chess/game/" + sessionKey);

	}
</script>

<div>
    <button onclick={handleCreateGame}>Create Game</button>
    <input bind:value={playerId}>
    <input bind:value={playerName}>
    <input bind:value={playerRating}>
</div>