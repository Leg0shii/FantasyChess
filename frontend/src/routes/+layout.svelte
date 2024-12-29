<script>
    let { children } = $props();
</script>

<nav>
	<a href="/">Home</a>
    <a href="/chess">Play Chess</a>
	<a href="/about">About</a>
</nav>

{@render children()}