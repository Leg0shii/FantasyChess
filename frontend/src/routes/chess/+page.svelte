<script lang="ts">
	let positions: { square: string; piece: string, color: string }[] = [];
	let playerWhite = '';
	let playerBlack = '';
	let sessionKey = '';

	async function createGame() {
		console.log("Creating game...");
		
		const res = await fetch("http://127.0.0.1:8000/game/create", {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ player_name: "Player White" })
		});

		console.log("Response status:", res.status);
        console.log("Response headers:", res.headers);

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

	// Variables to track the dragging state
	let draggingPiece: { square: string; piece: string; color: string } | null = null;
	let dragOffsetX = 0;
	let dragOffsetY = 0;

	let dragElement: HTMLElement | null = null;

	function handleMouseDown(event: MouseEvent, piece: { square: string; piece: string; color: string }) {
		event.preventDefault(); // Prevent native drag behavior

		draggingPiece = piece;
		positions = positions.filter((p) => p.square !== piece.square);

		// Track the offset of the cursor within the piece
		const target = event.currentTarget as HTMLElement;
		const rect = target.getBoundingClientRect();
		dragOffsetX = rect.width / 2;
		dragOffsetY = rect.height / 2;

		// Clone the piece element for dragging
		dragElement = target.cloneNode(true) as HTMLElement;
		dragElement.style.width = `${rect.width}px`;
		dragElement.style.height = `${rect.height}px`;
		dragElement.style.position = 'absolute';
		dragElement.style.pointerEvents = 'none';
		dragElement.style.zIndex = '1000';
		dragElement.style.backgroundSize = 'contain';
		dragElement.style.left = `${event.clientX - dragOffsetX}px`;
		dragElement.style.top = `${event.clientY - dragOffsetY}px`;
		dragElement.style.backgroundImage = getComputedStyle(target).backgroundImage;

		document.body.appendChild(dragElement);

		document.addEventListener('mousemove', handleMouseMove);
		document.addEventListener('mouseup', handleMouseUp);
	}

	function handleMouseMove(event: MouseEvent) {
		if (dragElement) {
			dragElement.style.left = `${event.clientX - dragOffsetX}px`;
			dragElement.style.top = `${event.clientY - dragOffsetY}px`;
		}
	}

	function handleMouseUp(event: MouseEvent) {
		// Determine the target square
		const target = document.elementFromPoint(event.clientX, event.clientY);
		if (target && target.dataset.square && draggingPiece) {
			const targetSquare = target.dataset.square;

			// Update the position of the dragged piece
			draggingPiece.square = targetSquare;
			positions = [...positions, draggingPiece];
		} else if (draggingPiece) {
			// Return the piece to its original position if dropped outside the board
			positions = [...positions, draggingPiece];
		}

		// Cleanup
		if (dragElement) {
			document.body.removeChild(dragElement);
			dragElement = null;
		}
		draggingPiece = null;

		document.removeEventListener('mousemove', handleMouseMove);
		document.removeEventListener('mouseup', handleMouseUp);
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
					class:bg-black={(r + f) % 2 === 1}
					data-square={`${file}${rank}`}
				>
					{#each positions.filter((p) => p.square === `${file}${rank}`) as piece}
						<piece
							class={`${piece.piece} ${piece.color}`}
							role="button"
							aria-label={`Piece ${piece.piece} ${piece.color}`}
							tabindex="0"
							on:mousedown={(event) => handleMouseDown(event, piece)}
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
		cursor: grab;
	}

	.chess-board piece:active {
		cursor: grabbing;
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

	.dragging {
		position: absolute;
		pointer-events: none;
		z-index: 1000;
	}
</style>
