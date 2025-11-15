<script lang="ts">
	import { onMount } from 'svelte';
	import washerImage from '$lib/assets/washer.jpg';

	let healthData: { status: string; service: string } | null = null;
	let loading = true;
	let error: string | null = null;

	async function fetchHealth() {
		try {
			loading = true;
			error = null;
			const response = await fetch('/api/health');
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			healthData = await response.json();
		} catch (e) {
			error = e instanceof Error ? e.message : 'Unknown error';
			console.error('Error fetching health:', e);
		} finally {
			loading = false;
		}
	}

	// Fetch on mount (client-side only)
	onMount(() => {
		fetchHealth();
	});
</script>

<div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
	<div class="max-w-md w-full bg-white rounded-lg shadow-lg p-6">
		<div class="flex flex-col items-center mb-6">
			<img 
				src={washerImage} 
				alt="Washer" 
				class="w-32 h-32 object-cover rounded-lg mb-4"
			/>
			<h1 class="text-3xl font-bold text-gray-900">LaundryPi</h1>
		</div>
		
		<div class="space-y-4">
			<h2 class="text-xl font-semibold text-gray-700">Server Health</h2>
			
			{#if loading}
				<div class="flex items-center space-x-2 text-gray-600">
					<svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
						<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
						<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
					</svg>
					<span>Checking health...</span>
				</div>
			{:else if error}
				<div class="bg-red-50 border border-red-200 rounded-md p-4">
					<p class="text-red-800 font-medium">Error</p>
					<p class="text-red-600 text-sm mt-1">{error}</p>
				</div>
				<button 
					on:click={fetchHealth}
					class="mt-2 px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
				>
					Retry
				</button>
			{:else if healthData}
				<div class="bg-green-50 border border-green-200 rounded-md p-4">
					<div class="flex items-center space-x-2 mb-2">
						<svg class="h-5 w-5 text-green-600" fill="currentColor" viewBox="0 0 20 20">
							<path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
						</svg>
						<p class="text-green-800 font-medium">{healthData.status}</p>
					</div>
					<p class="text-green-600 text-sm">Service: {healthData.service}</p>
				</div>
				<button 
					on:click={fetchHealth}
					class="mt-2 px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 transition-colors"
				>
					Refresh
				</button>
			{/if}
		</div>
	</div>
</div>
