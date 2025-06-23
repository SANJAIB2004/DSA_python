import heapq

def dijkstra(graph, start):
    # Step 1: Initialize all distances to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to start node is 0

    # Step 2: Use a priority queue to store (distance, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Step 3: Skip if a shorter path to current_node has been found
        if current_distance > distances[current_node]:
            continue

        # Step 4: Update distances to all neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Step 5: If new path is shorter, update and add to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example directed weighted graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

# Starting node
start_node = 'A'

# Call Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_node)

# Print results
print(f"Shortest distances from node {start_node}:")
for node in shortest_distances:
    print(f"{start_node} -> {node} = {shortest_distances[node]}")
