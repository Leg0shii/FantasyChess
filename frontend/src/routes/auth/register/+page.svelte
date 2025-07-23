<script lang="ts">
    import { authAPI } from "$lib/services/auth-api.js";

    let playerName = '';
    let password = '';
    
    async function register() {
        const response = await authAPI.register(playerName, password);
        if (response.success) {
            console.log("Registration successful");
        } else {
            console.error("Registration failed");
        }
    }
</script>

<div>
    <h1>Create your Chess Account!</h1>
    <img src="/images/register_image.png" height="300px" width="auto" alt="Chess" />

    <div>
        <input bind:value={playerName} placeholder="Username">
        <input bind:value={password} type="password" placeholder="Password">
        <button onclick={register}>Register</button>
    </div>
</div>