text = raw_input("Enter a string: ")
count = {}
for c in text:
	c = c.lower()
	if c.isalpha():
		if c not in count:
			count[c] = 1
		else:
			count[c] += 1

for c in count:
	print c + ":" + str(count[c]) + " ",