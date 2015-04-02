import sys

def necklace(a, b):
	c,d = a,b
	counter = 0
	sys.stdout.write(str(a) + " ")
	while(True):
		sum = (c + d) % 10
		c,d = d,sum
		sys.stdout.write(str(c) + " ")
		counter += 1
		if c == a and d == b:
			print d
			break
	print 'It took ' + str(counter) + ' times.'

for i in range(0,10):
	for j in range(0, 10):
		necklace(i, j)