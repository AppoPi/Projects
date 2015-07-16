import re

def mangle(string):
	#initialize list of which characters are capitalized
	caps = [False] * len(string)

	# check string for caps and store in 'caps'
	for i, x in enumerate(string):
		caps[i] = x.isupper()

	# split string into list of words
	words = re.findall("[A-z]+|\'|\"|\.|,|;|:|-| ", string.lower())

	# initialize list to store mangled words
	list1 = []
	for i in words:
		# mangled each word
		list1.append(''.join(sorted(i)))

	# create character list
	list2 = list(''.join(list1))
	
	# capitalize the originally capitalized indices
	for i, x in enumerate(list2):
		if caps[i]:
			list2[i] = list2[i].upper()
	
	# print mangled string
	print ''.join(list2)

mangle('This challenge doesn\'t seem so hard.')
mangle('There are more things between heaven and earth, Horatio, than are dreamt of in your philosophy.')
mangle('Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.')
mangle('Adder\'s fork, and Blind-worm\'s sting, Lizard\'s leg, and Howlet\'s wing.')
mangle('For a charm of powerful trouble, like a hell-broth boil and bubble.')

mangle('McDuck')