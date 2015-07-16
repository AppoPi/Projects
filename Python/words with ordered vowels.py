import re

file = 'enable1.txt'

with open(file, 'r') as f:
	wordlist = f.read().splitlines()

for i in wordlist:
	match = re.search('a[b-d|f-h|j-np-z]*e[b-df-hj-np-z]*i[b-df-hj-np-z]*o[b-df-hj-np-z]*u[b-df-hj-np-z]*y', i)
	if match:
		print match.group(0)