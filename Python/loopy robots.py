



x, y = 0, 0
d = 'N'

def walk(path):
	global x, y, d
	t = d
	c = ['N','E','S','W']
	for i in path.upper():
		if i == 'R':
			d = c[(c.index(d) + 1) % 4]
		elif i == 'L':
			d = c[(c.index(d) - 1) % 4]
	print 'Loop detected' if d != t  else 'No loop detected'

walk('S')
walk('RRL')
walk('SLLLRLSLSLSRLSLLLLS')