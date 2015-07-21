
def reverse(s):
	r = ''
	for i in s:
		r = i + r
	return r

def palindromic(i, max=50):
	f = i
	if str(i) == reverse(str(i)):
		return str(i) + ' gets palindromic after 0 steps: ' + str(i)
	
	s = str(i)
	for x in range(max):
		s = reverse(s)
		f += int(s)
		s = str(f)
		if str(f) == reverse(str(f)):
			return str(i) + ' gets palindromic after ' + str(x + 1) + ' steps: ' + str(f)
	return str(i) + ' did not get palindromic after ' + str(max) + ' steps: ' + str(f)

print palindromic(11)
print palindromic(68)
print palindromic(123)
print palindromic(286)
print palindromic(196196871)


