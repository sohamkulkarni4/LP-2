#A* algortihm

import heapq

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def heuristic(a,b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])
	
def a_star(maze,start,goal):
	rows, cols = len(maze), len(maze[0])
	open_list = []
	heapq.heappush(open_list,(0 + heuristic(start,goal), 0, start, []))
	visited = set()
	
	while open_list:
		f, g, current, path = heapq.heappop(open_list)
		
		if current == goal:
			return path + [current]
		
		visited.add(current)
		
		for move in moves:
			new_r, new_c = current[0] + move[0] , current[1] + move[1]
			
			if 0 <= new_r < rows and 0<= new_c < cols and maze[new_r][new_c] == 0:
				neighbour = (new_r, new_c)
				if neighbour not in visited:
					new_g = g+1
					new_f = new_g + heuristic(neighbour,goal)
					heapq.heappush(open_list, (new_f, new_g, neighbour, path + [current]))
	return None
	
maze = [
	[0, 1, 0, 0, 0],
	[0, 1, 0, 1, 0],
	[0, 0, 0, 1, 1],
	[0, 1, 1, 1, 0],
	[0, 0, 0, 0, 0]
]

start = (0,0)
goal = (4,4)

path = a_star(maze, start, goal)

for i in range (5):
	print(maze[i])		

if path:
	print("\nPath Found !!!!")
	print(path,"\n")
else:
	print("\npath not found \n")
		

