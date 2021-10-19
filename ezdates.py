months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}

def fixdate(given, format="mdy"):
	found = [0, 0, 0] #d,m,y
	splitdate = given.split(" ")
	if len(splitdate) != 3: return None
	splitdate = [[splitdate[0], 2, 2, 2], [splitdate[1], 2, 2, 2], [splitdate[2], 2, 2, 2]]
	for value in splitdate:
		if value[0] > 31:
			value[3] = 1
	return splitdate