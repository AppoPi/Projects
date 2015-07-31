
def sumSquare(n):
	i = 0
	while(n > 0):
		i += (n % 10) * (n  % 10)
		n /= 10
	return i

def happy(n):
	list = []
	while(n != 1):
		n = sumSquare(n)
		if n not in list:
			list.append(n)
		else:
			return 'Sad'
	return 'Happy'

# print happy(12)
# print happy(13)
# print happy(740) # Sad
# print happy(836) # Happy

a = 0
for i in range(1, 1001):
	if happy(i) == 'Happy':
		a += 1
print a