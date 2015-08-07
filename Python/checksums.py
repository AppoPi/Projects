

s = 'Fletcher'

def fletcher16(s):
	sum1 = sum2 = count = 0
	for i in range(len(s)):
		sum1 = (sum1 + ord(s[i])) % 255
		sum2 = (sum2 + sum1) % 255
	return format(sum2 << 8 | sum1, 'x').upper()
	
def input(s):
	s = s.split('\n')

	news = ''
	for i in range(1, len(s)):
		news += fletcher16(s[i]) + '\n'
	return news

print input('''3
Fletcher
Sally sells seashells by the seashore.
Les chaussettes de l'archi-duchesse, sont-elles seches ou archi-seches ?''')