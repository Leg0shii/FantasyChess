<script>
    let { children } = $props();
</script>

<svelte:head>
	<link rel="stylesheet" href="/chess-pieces/black-pieces.css" />
	<link rel="stylesheet" href="/chess-pieces/white-pieces.css" />
</svelte:head>

<nav>
	<a href="/">Home</a>
    <a href="/chess">Play Chess</a>
	<a href="/about">About</a>
</nav>

{@render children()}