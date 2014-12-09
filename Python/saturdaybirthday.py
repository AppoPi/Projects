
#Calculate the next year a given date falls on a Saturday
#d = 1-31
#m = 1-12 (3-14)
#y = XXXX

def getDayOfWeek(d, m, y):
	if m in (1,2):
		y -= 1
	#loop through year
	# while True:
	m = (m - 2)
	m = m + 12 if m < 1 else m
	c = y / 100
	y = y % 100
	w = (d + 2.6 * m - 0.2 + y + y/4 + c/4 - 2*c) % 7
	return int(w)

	# return  0

print getDayOfWeek(1,1,2014)

# print "Expected: 1/1/1972"

# 1/1/1970 Thursday (4)