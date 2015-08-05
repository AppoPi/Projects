import math

def button(input):
	list = []
	input = input[input.index('\n')+1:]
	for i in input.split('\n'):
		a = i.split(':')
		list.append([a[0], float(a[1])])

	list = sorted(list,key=lambda a:a[1])

	newlist = []
	last = 0
	for i,x in enumerate(list):
		if i == 0:
			last = int(math.floor(60 - list[i][1]))
			newlist.append(last)
		else:
			last = int(math.floor(60 - list[i][1] + list[i-1][1]))
			newlist.append(last)
	s = ''
	for i in range(len(list)):
		s += '{0}: {1}\n'.format(list[i][0],newlist[i])
	return s


input1 = '''8
Coder_d00d: 3.14
Cosmologicon: 22.15
Elite6809: 17.25
jnazario: 33.81
nint22: 10.13
rya11111: 36.29
professorlamp: 31.60
XenophonOfAthens: 28.74'''	

input2 = '''7
bholzer: 101.09
Cosmologicon: 27.45
nint22: 13.76
nooodl: 7.29
nottoobadguy: 74.56
oskar_s: 39.90
Steve132: 61.82'''

print button(input1)
print button(input2)