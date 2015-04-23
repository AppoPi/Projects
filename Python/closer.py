#http://codereview.stackexchange.com/questions/86754/given-two-int-values-return-the-one-closer-to-10

def closer(a, b, c):
	if a == b:
		return 0
	elif abs(a - c) < abs(b - c):
		return a
	elif abs(a - c) > abs(b-c):
		return b
	else:
		return a,b
	
def printCloser(a, b, c):
	if a == closer(a, b, c):
		return str(a) + ' is closer to ' + str(c) + ' than ' + str(b)
	elif b == closer(a, b, c):
		return str(b) + ' is closer to ' + str(c) + ' than ' + str(a)
	else:
		return str(a) + ' and ' + str(b) + ' are equally close to ' + str(c)

a = 8
b = 13
c = 10
print printCloser(a, b, c)

a = 9
b = 21
c = 17
print printCloser(a, b, c)

a = 8
b = 12
c = 10
print printCloser(a, b, c)