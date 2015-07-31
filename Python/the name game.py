import re

def namegame(n):
	if re.match('b[a-z]+', n, re.IGNORECASE): # starts with b
		return '{0}, {1}, bo-{2},\nBonana fanna fo F{3},\nFee fy mo M{4},\n{5}!\n'''.format(n, n, n[1:], n[1:], n[1:], n)
	elif re.match('f[a-z]+', n, re.IGNORECASE): # starts with f
		return '{0}, {1}, bo B{2},\nBonana fanna Fo-{3},\nFee fy mo M{4},\n{5}!\n'''.format(n, n, n[1:], n[1:], n[1:], n)
	elif re.match('m[a-z]+', n, re.IGNORECASE): # starts with m
		return '{0}, {1}, bo B{2},\nBonana fanna fo F{3},\nFee fy Mo-{4},\n{5}!\n'''.format(n, n, n[1:], n[1:], n[1:], n)
	elif not re.match('^[aeiou][a-z]+', n, re.IGNORECASE): # starts with a vowel
		return '{0}, {1}, bo B{2},\nBonana fanna fo F{3},\nFee fy mo M{4},\n{5}!\n'.format(n, n, n[1:], n[1:], n[1:], n)
	else:
		l = n.lower()
		return '{0}, {1}, bo B{2},\nBonana fanna fo F{3},\nFee fy mo M{4},\n{5}!\n'.format(n, n, l, l, l, n)

print namegame('Lincoln')
print namegame('Nick')
print namegame('Arnold')
print namegame('Billy')
print namegame('Bob')
print namegame('Fred')
print namegame('Mary')
print namegame('Jesse')
print namegame('Jay')
print namegame('Finley')