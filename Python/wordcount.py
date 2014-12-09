import sys
import re, string
import operator


def strip(word):
	return re.sub(r'[\W_]+', '',word)


input = sys.argv[1]

f = open(input, 'r')

dict = {}
int = 0
for line in f:
	words = line.split()
	for w in words:
		w = strip(w).lower()
		if w in dict:
			dict[w] += 1
		else:
			dict[w] = 1
	
f.close()

print dict