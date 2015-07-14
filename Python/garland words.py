

def garland(word):
	count, max = 0, 0
	for i in range(1, len(word)):
		if word[:i] == word[len(word)-i:]:
			max = len(word[:i])
	return word + ' -> ' + str(max)
	
print garland('programmer')
print garland('ceramic')
print garland('onion')
print garland('alfalfa')