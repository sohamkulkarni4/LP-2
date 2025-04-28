import heapq

def dijkstra(graph, source):
    num_nodes = len(graph)
    shortest_distances = [float('inf')] * num_nodes
    shortest_distances[source] = 0

    priority_queue = [(0, source)]  

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        
        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance_through_current = current_distance + weight

            if distance_through_current < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance_through_current
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    return shortest_distances


graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(2, 4), (3, 14), (4, 10), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}

source_node = 0
shortest_paths = dijkstra(graph, source_node)
print(f"Shortest distances from node {source_node}:", shortest_paths)

# O(|E| + |V|log|V|)

