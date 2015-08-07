

def islands(s):
	last = out = ''
	for i in range(len(s)):
		if last != s[i]:
			if s[i] == s[i+1]:
				last = s[i]
				out += s[i] + ':' + str(i) + ' '
	return out

s = 'proogrrrammminggg'
print islands(s)