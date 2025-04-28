def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, assignment, node=0):
    if node == len(graph):
        return True

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            if graph_coloring(graph, colors, assignment, node + 1):
                return True
            assignment.pop(node)  # Backtrack

    return False

def solve_graph_coloring(graph, k):
    colors = [i for i in range(1, k + 1)]  # Colors are 1,2,3,...k
    assignment = {}

    if graph_coloring(graph, colors, assignment):
        print("Color Assignment Possible:")
        for node in sorted(assignment.keys()):
            print(f"Node {node}: Color {assignment[node]}")
    else:
        print("No valid coloring possible with", k, "colors.")


graph = {
	0: [2,1],
	1: [0,5,4],
	2: [0,3],
	3: [2,5],
	4: [1],
	5: [1,3,6],
	6: [5]
}

solve_graph_coloring(graph, k=3)

