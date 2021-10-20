months = {"january":1, "february":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october":10, "hey":1}
found = [0, 0, 0] #d,m,y    0 = no   1 = yes   2 = possible
splitdate = None

def preformat():
	global splitdate
	global found
	global months
	for i in range(len(splitdate)):
		try:
			if int(splitdate[i][0]) <= 12:
				splitdate[i][0]= int(splitdate[i][0])
				splitdate[i][2] = 1
				break
		except:
			for month in months:
				if splitdate[i][0].lower() in month:
					splitdate[i][0] = months[month]
					if found[1] != 0: return None
					found[1] = 1 
					splitdate[i][2] = 1
					break
def getmonth():
	global splitdate
	for l in splitdate:
		if l[2] == 1:
			return l[0]
def getday():
	global splitdate
	for l in splitdate:
		if l[1] == 1:
			return l[0]
def getyear():
	global splitdate
	for l in splitdate:
		if l[3] == 1:
			return l[0]
def fixdate(given, format="mdy"):
	global splitdate
	global found
	splitdate = given.split(" ")
	if len(splitdate) != 3: return None
	splitdate = [[splitdate[0], 2, 2, 2], [splitdate[1], 2, 2, 2], [splitdate[2], 2, 2, 2]] # splitdate[x][0] = value | [1] = day   [2] = month   [3] = year
	preformat()
	for value in splitdate: #determines year
		if int(value[0]) > 31:
			value[3] = 1
			if found[2] != 0: return None
			found[2] = 1
	for value in splitdate: 
		i = 0
		for item in value:
			if item != value[0]:
				if item != 1:
					i+=1
		if i < 3:
			pass
		else:
			index = 0
			for item in found:
				if item == 0:
					value[item+1] = 1
	format = list(format)
	final = []
	for thing in format:
		if thing == "m":
			final.append(str(getmonth()))
		elif thing == "d":
			final.append(str(getday()))
		elif thing == "y":
			thingi = int(getyear())
			if thingi < 100:
				thingi = "20" + str(getyear())
			final.append(str(thingi))
	return "-".join(final)
