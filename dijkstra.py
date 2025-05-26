import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]  # Priority queue to hold nodes to explore their current distances
    dist = {start: 0}  # Dictionary to store the shortest distance from `start` to each node
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)  # Get node with the smallest distance
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u].items():  # Explore neighboring nodes
            distance = current_dist + weight
            if distance < dist.get(v, float('inf')):  # Update distance if a shorter path is found
                dist[v] = distance
                heapq.heappush(min_heap, (distance, v))  # Push the updated distance to the priority queue
    return dist

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
