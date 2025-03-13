import heapq

# Sample graph as an adjacency list with both positive and negative weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': -3},
    'D': {'B': 5, 'C': 1, 'E': 2},
    'E': {'D': 2, 'F': 3},
    'F': {'E': 3, 'A': 1},
    'G': {'F': 1},
    'H': {'G': -4}
}


def dijkstra(graph, source):
    # Initialize distances with infinity and set source to 0
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    # Process nodes in priority order
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the node was already processed with a shorter distance
        if current_distance > distances[current_node]:
            continue

        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def bellman_ford(graph, source):
    # Initialize distances with infinity and set source to 0
    distances = {node: float('inf') for node in graph}
    distances[source] = 0

    # Relax edges up to |V| - 1 times
    for i in range(len(graph) - 1):
        updated = False
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    updated = True
        # Early exit if no updates were made in this pass
        if not updated:
            break

    # Check for negative-weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                print("Graph contains a negative-weight cycle")
                return None

    return distances


# Unified function to display results
def display_shortest_paths(graph, source):
    print(f"Shortest paths from {source} using Dijkstra's Algorithm:")
    dijkstra_result = dijkstra(graph, source)
    if dijkstra_result:
        for node, distance in dijkstra_result.items():
            print(f"Node {node}: {distance}")

    print(f"\nShortest paths from {source} using Bellman-Ford Algorithm:")
    bellman_ford_result = bellman_ford(graph, source)
    if bellman_ford_result:
        for node, distance in bellman_ford_result.items():
            print(f"Node {node}: {distance}")


# Test with the sample source node
source_node = 'A'
display_shortest_paths(graph, source_node)
