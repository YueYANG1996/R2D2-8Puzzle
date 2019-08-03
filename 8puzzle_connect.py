def connect_to_all(Robots):
	droid1 = DroidClient()
	droid2 = DroidClient()
	droid3 = DroidClient()
	droid4 = DroidClient()
	droid5 = DroidClient()
	droid6 = DroidClient()
	droid7 = DroidClient()
	droid8 = DroidClient()
	Droids = [droid1, droid2, droid3, droid4, droid5, droid6, droid7, droid8]
	for key in Robots:
		Droids[key - 1].connect_to_droid(Robots[key])
	return Droids