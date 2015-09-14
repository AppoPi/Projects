import math

n1,n2 = 1,0
while n1 != n2:
	n1 = n2
	n2 = math.cos(n2)
print n2