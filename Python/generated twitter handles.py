# Parse words from file
words = []
with open ('enable1.txt') as f:
	words = f.read().split('\n')

# Find words that start with 'at'
at = []
for i in words:
	if i.startswith('at'):
		at.append('@' + i[2:])

# Insertion Sort
for i in range(1, len(at) - 1):
	j = i
	while j > 0 and len(at[j-1]) > len(at[j]):
		at[j], at[j-1] = at[j-1], at[j]
		j -= 1

print 'Ten shortest: '
for i in at[:10]:
	print i + ' : ' + i.replace('@', 'at')
	
print 'Ten longest: '
for i in at[-10:]:
	print i + ' : ' + i.replace('@', 'at')