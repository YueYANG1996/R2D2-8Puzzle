def action(droid, direction, speed, time):
	if direction == 'east':
		droid.roll(speed, 90, time)
	elif direction == 'south':
		droid.roll(speed, 180, time)
	elif direction == 'west':
		droid.roll(speed, 270, time)
	else:
		droid.roll(speed, 0, time)
	droid.roll(0, 0, 0)
