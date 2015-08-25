
def gcf(a, b):
	while a > 0 and b > 0:
		if a > b:
			a = a % b
		elif a < b:
			b = b % a
		else:
			return a
	return max(a,b)

def lcm(a, b):
	return a * b / gcf(a, b)

def reduce(fraction):
	numerator = int(fraction[:fraction.index('/')])
	denominator = int(fraction[fraction.index('/') + 1:])
	g = gcf(numerator, denominator)
	return str(numerator/g) + '/' + str(denominator/g)

def add(a, b):
	anum = int(a[:a.index('/')])
	aden = int(a[a.index('/') + 1:])
	bnum = int(b[:b.index('/')])
	bden = int(b[b.index('/') + 1:])
	
	num = str(lcm(aden, bden) / aden * anum + lcm(aden, bden) / bden * bnum)
	den = str(lcm(aden, bden))
	return reduce(num + '/' + den)

def addAll(frac):
	f = frac.split('\n')[1:]
	a = '0/1'
	for i in f:
		a = add(a, i)
	print a

addAll('''2
1/6
3/10''')

addAll('''3
1/3
1/4
1/12''')

addAll('''5
2/9
4/35
7/34
1/2
16/33''')

addAll('''10
1/7
35/192
61/124
90/31
5/168
31/51
69/179
32/5
15/188
10/17''')