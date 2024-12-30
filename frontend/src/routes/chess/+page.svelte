<script lang="ts">
	let positions: { square: string; piece: string, color: string }[] = [];
	let playerWhite = '';
	let playerBlack = '';
	let sessionKey = '';

	async function createGame() {
		// Call the API to create a new game
		const res = await fetch("http://127.0.0.1:8000/game/create", {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ player_name: "Player White" })
		});
		const data = await res.json();
		sessionKey = data.session_key;
		loadGameState();
	}

	async function joinGame() {
		const inputKey = prompt("Enter the session key to join:");
		if (!inputKey) return;

		const res = await fetch("http://127.0.0.1:8000/game/join", {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ session_key: inputKey, player_name: "Player Black" })
		});
		if (res.status === 404 || res.status === 400) {
			alert(await res.json().detail); // Show error from backend
			return;
		}
		sessionKey = inputKey;
		loadGameState();
	}

	async function loadGameState() {
		// Fetch the game state and load player names and positions
		const res = await fetch(`http://127.0.0.1:8000/game/state?session_key=${sessionKey}`);
		const data = await res.json();
		console.log(data);
		positions = data.game_state.chess_board;
		playerWhite = data.game_state.players[0].name;

		if (data.game_state.players.length === 2)
			playerBlack = data.game_state.players[1].name;
	}

	const ranks = [8, 7, 6, 5, 4, 3, 2, 1];
	const files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

	// To track the piece being dragged
	let draggedPiece: { square: string; piece: string; color: string } | null = null;

	function handleDragStart(event: DragEvent, piece: { square: string; piece: string; color: string }) {
		draggedPiece = piece;
		event.dataTransfer?.setData('application/json', JSON.stringify(piece));
		event.dataTransfer!.effectAllowed = 'move';
	}

	// Function to handle dropping a piece
	function handleDrop(event: DragEvent, targetSquare: string) {
		event.preventDefault();
		const pieceData = event.dataTransfer?.getData('application/json'); // Retrieve the piece data
		if (!pieceData) return;

		const draggedPiece = JSON.parse(pieceData);
		const draggedSquare = draggedPiece.square;

		if (draggedPiece && draggedSquare !== targetSquare) {
			draggedPiece.square = targetSquare;
			positions = positions.filter((p) => p.square !== draggedSquare);
			positions = [...positions, draggedPiece];
		}

		
	}

	function allowDrop(event: DragEvent) {
		event.preventDefault();
	}

</script>

<div>
	<div class="players">
		<div>White: {playerWhite}</div>
		<div>Black: {playerBlack}</div>
	</div>

	<div class="chess-board">
		{#each ranks as rank, r}
			{#each files as file, f}
				<div
					role="gridcell"
					aria-label={`Square ${file}${rank}`}
					tabindex="0"
					draggable="false"
					class:bg-black={(r + f) % 2 === 1}
					on:dragover={allowDrop}
					on:drop={(event) => handleDrop(event, `${file}${rank}`)}
				>
					{#each positions.filter((p) => p.square === `${file}${rank}`) as piece}
						<piece
							class={`${piece.piece} ${piece.color}`}
							draggable="true"
							role="button"
							aria-label={`Piece ${piece.piece} ${piece.color}`}
							tabindex="0"
							on:dragstart={(event) => handleDragStart(event, piece)}
						></piece>
					{/each}
				</div>
			{/each}
		{/each}
	</div>

	<div class="controls">
		<button on:click={createGame}>Create Game</button>
		<button on:click={joinGame}>Join Game</button>
	</div>
</div>

<style>
	.players {
		display: flex;
		justify-content: space-between;
		font-weight: bold;
		margin-bottom: 1em;
	}

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

	.controls {
		margin-top: 1em;
		display: flex;
		gap: 1em;
		justify-content: center;
	}

	.chess-board piece:active {
		cursor: grabbing;
	}
</style>
