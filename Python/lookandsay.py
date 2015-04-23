#look and say sequence

def count(string):
	if len(string) == 1:
		return '1' + string

	out = ''
	i = 0
	count = 1
	prev = string[0]
	for i in range(len(string)):
		if i == 0:
			prev = string[0]
		else:
			if string[i] == prev:
				count += 1
				if i == len(string) - 1:
					out += str(count) + prev
			else:
				out +=  str(count) + str(prev)
				prev = string[i]
				count = 1
				if i == len(string) - 1:
					out +=  "1" + prev
	return out

def look(i):
	if i < 1:
		return '1'
	elif i == 1:
		return '11'
	else:	
		out = ''
		s = count('1')
		for i in range(i):
			out = s + '\n'
			s = count(s)
		return out[:-1]

for i in range(15):
	print look(i)
