#BFS AND DFS

graph = {
	0: [2,1],
	1: [0,5,4],
	2: [0,3],
	3: [2,5],
	4: [1],
	5: [1,3,6],
	6: [5]
}



def dfs(graph, start_node):
	visited[start_node] = True
	
	print(start_node)
	
	for c in graph[start_node]:
		if not visited[c]:
			dfs(graph,c)

def bfs(graph,start_node):
	queue = [start_node]
	visited = [start_node]
	
	while queue:
		cur = queue.pop(0)
		print(cur)
		for c in graph[cur]:
			if c not in visited:
				queue.append(c)
				visited.append(c) 

print("BFS search of graph is:")

bfs(graph,0)




visited = [0] * 7
print("\n\nDFS search of graph is:")

dfs(graph,0)




