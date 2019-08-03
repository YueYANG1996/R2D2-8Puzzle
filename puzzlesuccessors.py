import copy
def successors(puzzle):
	for i in range(len(puzzle)):
		for j in range(len(puzzle[0])):
			if puzzle[i][j] == None:
				blank_pos = (i, j)
				break
	x = blank_pos[0]
	y = blank_pos[1]
	expand_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	successor = []
	for direction in expand_direction:
		expand_node = (x + direction[0], y + direction[1])
		current_lst = copy.deepcopy(puzzle)
		exchange_puzzle = exchange(current_lst, x, y, expand_node[0], expand_node[1])
		if exchange_puzzle != None:
		    if direction == (1, 0):
		        move = 'north'
		    elif direction == (0, 1):
		        move = 'west'
		    elif direction == (-1, 0):
		        move = 'south'
		    else:
		        move = 'east'
		    move_num = puzzle[expand_node[0]][expand_node[1]]
		    append_state = (exchange_puzzle, move_num, move)
		    successor.append(append_state)
	return successor
    
def exchange(puzzle, x1, y1, x2, y2):
	current_lst = copy.deepcopy(puzzle)
	if 0 <= x2 < len(current_lst) and 0 <= y2 < len(current_lst[0]):
		temp = copy.deepcopy(current_lst)
		temp[x1][y1] = current_lst[x2][y2]
		temp[x2][y2] = current_lst[x1][y1]
		return temp
	else:
		return None

		
