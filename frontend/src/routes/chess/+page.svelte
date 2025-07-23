<script lang="ts">
    import { goto } from "$app/navigation";
	import { chessAPI } from "$lib/services/chess-api.js";
    import { authAPI } from "$lib/services/auth-api.js";

    let playerName = '';
    let password = '';

    async function handleCreateGame() {
		const data = await chessAPI.createGame({
            player: {
                name: playerName,
                rating: 0
            }
        });

        const sessionKey = data.session_key;
        goto("/chess/game/" + sessionKey);

	}

    async function login() {
        const response = await authAPI.login(playerName, password);
        if (response.success) {
            console.log("Login successful");
        } else {
            console.error("Login failed");
        }
    }

    async function register() {
        goto("/auth/register");
    }
</script>

<div>
    {#if authAPI.isAuthenticated()}
        <p>Welcome!</p>
        <button onclick={handleCreateGame}>Create Game</button>
        <input bind:value={playerName}>
        <input bind:value={password} type="password" placeholder="Password">
    {:else}
        <p>Please log in to play chess.</p>
        <button onclick={login}>Log In</button>
        <button onclick={register}>Register</button>
    {/if}
</div>