<script lang='ts'>
	let positions: { square: string; piece: string }[] = [];

    async function fetchPositions() {
		const res = await fetch("http://127.0.0.1:8000/api/positions");
        const data = await res.json();
        positions = data;
	}

	function onMove() {
		fetchPositions();
	}

	const ranks = [8,7,6,5,4,3,2,1];
	const files = ['a','b','c','d','e','f','g','h'];
</script>

<div class="chess-board">
	{#each ranks as rank, r}
		{#each files as file, f}
			<div class:bg-black={(r + f) % 2 === 1}>
                {#if positions.some((p) => p.square === file + rank)}
                    <piece class={positions.find((p) => p.square === file + rank)?.piece}></piece>
                {/if}
			</div>
		{/each}
	{/each}
</div>

<button on:click={onMove}>Load</button>

<style>
    .chess-board piece {
        width: 100%; 
        height: 100%;
        background-size: contain;
        display: block;
    }

	.chess-board {
        width: 32em; 
        height: 32em;
		display: grid;
		grid-template-columns: repeat(8, 4em);
		grid-template-rows: repeat(8, 4em);
		border: 1px solid black;
		aspect-ratio: 1;

		.bg-black {
			background: gray;
		}
	}
</style>