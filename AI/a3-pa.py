import heapq

def prim_mst(graph, start=0):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, start)]  
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += weight

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    
    return total_cost


graph = {
    0: [(1, 4), (7, 8)],
    1: [(0, 4), (2, 8), (7, 11)],
    2: [(1, 8), (3, 7), (8, 2), (5, 4)],
    3: [(2, 7), (4, 9), (5, 14)],
    4: [(3, 9), (5, 10)],
    5: [(4, 10), (3, 14), (2, 4), (6, 2)],
    6: [(5, 2), (7, 1), (8, 6)],
    7: [(0, 8), (1, 11), (6, 1), (8, 7)],
    8: [(2, 2), (6, 6), (7, 7)]
}
print("Total cost of MST:", prim_mst(graph))


# O( VlogV + ElogV)

