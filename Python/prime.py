import sys

# single line comment

""" this is a multiline comment
  which spawns many lines
"""


if not sys.argv[1:]:
	num = int(input('Enter an integer: '))
else:
	num = int(sys.argv[1])

def isPrime(input):
	if input<2: 
		return False
	for n in range(2, input-1):
		if input%n==0:
			return False
	return True

for n in range(2, num):
	if isPrime(n):
		print (str(n),  end=", ")
	