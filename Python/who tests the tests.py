
tests = '''6
0 Car raC
0 Alpha AhplA
0 Discuss noissucsiD
1 Batman BATMAN
1 Graph GRAPH
1 One one'''

# def reverse(s):
	# if len(s) > 0:
		# return s[-1] + reverse2(s[:-1])
	# return ''

def re(s):
	r = ''
	for i in s:
		r = i + r
	return r

for i in tests.split('\n')[1:]:
	a, b, c = i.split(' ')
	if a == '0':
		print 'Good test data' if re(b) == c else 'Mismatch! Bad test data'
	elif a == '1':
		print 'Good test data' if b.upper() == c else 'Mismatch! Bad test data'