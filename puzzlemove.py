from puzzleaction import action
def move_puzzle(all_robots, path, ROBOTS):
	for movement in path:
		robot_num = movement[0]
		direction = movement[1]
		droid = all_robots[robot_num - 1]
		if droid.connected_to_droid == True:
			action(droid, direction, 0.3, 2.2)
		else:
			droid.connect_to_droid(ROBOTS[robot_num])
			if droid.connected_to_droid == True:
				action(droid, direction, 0.3, 2.2)
			else:
				for robot in all_robots:
					if robot.connected_to_droid == True:
						robot.disconnect()
						break
				droid.connect_to_droid(ROBOTS[robot_num])
				action(droid, direction, 0.3, 2.2)
	droid.animate(10)
	pass
