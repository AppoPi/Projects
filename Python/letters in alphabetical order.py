
def isOrdered(s):
	a = 0
	for i in range(1, len(s)):
		if s[i] < s[i - 1]:
			a += 1
	if a == len(s) - 1:
		return s + ' REVERSE ORDER'
	elif a == 0:
		return s + ' IN ORDER'
	else:
		return s + ' NOT IN ORDER'

print isOrdered('almost')
print isOrdered('cereal')
print isOrdered('billowy')
print isOrdered('biopsy')
print isOrdered('chinos')
print isOrdered('defaced')
print isOrdered('chintz')
print isOrdered('sponged')
print isOrdered('bijoux')
print isOrdered('abhors')
print isOrdered('fiddle')
print isOrdered('begins')
print isOrdered('chimps')
print isOrdered('wronged')