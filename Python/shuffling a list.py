import random
from random import shuffle

def library(list):
	# Slice list so that function doesn't alter parameter list
	newlist = list[:]
	# Call random library shuffle to randomize list order
	shuffle(newlist)
	return newlist

# Perfectly alternate from each half of the list
def faro(list):
	r = []
	# Divide list into two halves
	l1 = list[:len(list)/2]
	l2 = list[len(list)/2:]
	# Alternate between each half
	for (i, x) in zip(l1, l2):
		# Create new list from alternating elements of the two halves
		r.append(i)
		r.append(x)
	# Add back in the odd element
	if len(list) % 2 == 1:
		r.append(list[-1])
	return r

# Remove at random from the list until there are none remaining
def fisherYates(list):
	r = []
	while(len(list) > 0):
		# Generate random number
		i = random.randint(0, len(list)-1)
		# Add to list
		r.append(list[i])
		# Remove ("strikeout") random element 
		del list[i]
	return r

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = ['apple','blackberry','cherry','dragonfruit','grapefruit','kumquat','mango','nectarine','persimmon','raspberry']
list3 = ['a','e','i','o','u']

lists = [list1, list2, list3]

for i in lists:
	# random library shuffle
	print library(i)
	# Faro shuffle
	print faro(i)
	# Fisher And Yates shuffle
	print fisherYates(i)
