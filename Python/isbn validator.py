import re
import random
import string

# Validates 10 digit ISBN's
def valid(isbn):
	sum = 0
	isbn = re.sub('[- ]', '', isbn)
	l = len(isbn)
	if re.match('[0-9]{9}[x]', isbn, flags=re.IGNORECASE):
		for i in range(l-1):
			sum += int(isbn[i]) * (l - i)
		return (sum + 10) % 11 == 0
	elif re.match('[0-9]{10}', isbn):
		for i in range(l):
			sum += int(isbn[i]) * (l - i)
		return sum % 11 == 0
	return False

def generate():
	isbn = ''.join(random.choice(string.digits) for _ in range(9))
	sum = 0
	l = len(isbn)
	for i in range(l):
		sum += int(isbn[i]) * (l - i + 1)
	digit = (11 - (sum % 11)) % 11
	if digit != 10:
		return isbn + str(digit)
	else:
		return isbn + 'X'

a = '0-7475-3269-9'
print  a + ' is valid :' + str(valid(a))
b = '074753277X'
print b + ' is valid: ' + str(valid(b))
c = generate()
print 'Generated: ' + c
print c + ' is valid: ' + str(valid(c))
