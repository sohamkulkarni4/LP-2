class DisjointSet:
    def __init__(self, num_nodes):
        self.parent = [i for i in range(num_nodes)]
        self.rank = [0] * num_nodes

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False  

        
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root2] < self.rank[root1]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        return True

def kruskal_mst(edges, num_nodes):
    
    edges.sort(key=lambda edge: edge[2])  
    disjoint_set = DisjointSet(num_nodes)
    
    mst_weight = 0
    mst_edges = []

    for node1, node2, weight in edges:
        if disjoint_set.union(node1, node2):
            mst_weight += weight
            mst_edges.append((node1, node2, weight))

    return mst_weight, mst_edges


edges = [
    (0, 1, 4), (0, 7, 8),
    (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 8, 2), (2, 5, 4),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1), (6, 8, 6),
    (7, 8, 7)
]

num_nodes = 9
mst_cost, mst_edges = kruskal_mst(edges, num_nodes)

print("Total cost of MST:", mst_cost)
print("Edges in the MST:", mst_edges)

