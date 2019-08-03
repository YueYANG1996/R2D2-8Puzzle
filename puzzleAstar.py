import copy
import math
import queue
from puzzlesuccessors import successors

def find_solution(start, goal):
	dic = {1: (0,0), 2: (0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1)}
	rows = len(start)
	cols = len(start[0])
	node_visited = []
	q = queue.PriorityQueue()
	h = 0
	for i in range(len(start)):
		for j in range(len(start[0])):
			if start[i][j] != start[i][j] and start[i][j] != None:
				actual_pos = dic[start[i][j]]
				m_d = abs(i - actual_pos[0]) + abs(j - actual_pos[1])
				h += m_d
	astar_cost_start = h
	cost_start = 0
	path = []
	q.put((astar_cost_start, cost_start, path, start))

	while q.empty() != True:
		current_node = q.get()
		astar_cost, current_cost, path, current_pos = current_node[0], current_node[1], current_node[2], current_node[3]
		if current_pos == goal:
			return path

		if current_pos not in node_visited:
			node_visited.append(current_pos)
			for child in successors(current_pos):
				expand_pos = child[0]
				move_node = child[1]
				move_direction = child[2]
				expand_cost = current_cost + 1
				h = 0
				for i in range(len(start)):
					for j in range(len(start[0])):
						if expand_pos[i][j] != goal[i][j] and expand_pos[i][j] != None:
							actual_pos = dic[expand_pos[i][j]]
							m_d = abs(i - actual_pos[0]) + abs(j - actual_pos[1])
							h += m_d
				heuristic = h
				expand_astar_cost = expand_cost + heuristic
				new_state = (expand_astar_cost, expand_cost, path + [(move_node, move_direction)], expand_pos)
				q.put(new_state)



