import re

with open('haystack.txt', 'r') as f:
	text = f.read().split('\n')

pat = '^[b-df-hj-np-z]+[ .,]+| [b-df-hj-np-z]+[ .,]| [b-df-hj-np-z]$|[aeiou]{4}|[b-df-hj-np-z]{5}'
count = 1

for line in text:
	
	result = re.search(pat, line)
	if not result:
		# count += 1
		print line
# print count