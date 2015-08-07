import binascii

def string2binary(s):
	ret = ''
	for i in s:
		ret += bin(ord(i)).replace('b','')
	return ret

def binary2string(s):
	ret = ''
	for i in range(len(s)/8):
		ret += chr(int(s[8*i:8*i + 8],2))
	return ret

def bitwiseOr(s, mask):
	ret = ''
	for i in range(len(s)):
		ret += chr(ord(s[i]) ^ ord(mask[i]))
	return ret

seed = None

if seed == None:
	seed = 1103515245

def random():
	global seed
	ret = (21403 * seed + 2531011) % 2**31
	seed = ret
	return ret

i = 'abc'
m = str(random())
print 'Original: ' + i
print 'Encoded: ' + bitwiseOr(i, m)
print 'Decoded: ' + bitwiseOr(bitwiseOr(i, m), m)
