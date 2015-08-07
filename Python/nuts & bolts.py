

catalog = []


def update(s):
	# check catalog for item
	for index, val in enumerate(catalog):
		if s[:s.index(' ')] in val:
			name = s[:s.index(' ')]
			new_price = int(s[s.index(' ') + 1:])
			catalog[index][2] = new_price
			return
	# add item to catalog
	name = s[:s.index(' ')]
	original_price = int(s[s.index(' ') + 1:])
	catalog.append([name, original_price, original_price])
	
def clear():
	del catalog[:]

def printChanges():
	for i in catalog:
		if i[1]  != i[2]:
			diff = i[2] - i[1]
			if diff < 0:
				print i[0] + ' ' + str(i[2] - i[1])
			else:
				print i[0] + ' +' + str(i[2] - i[1])
	
def processInput(s):
	s = s.split('\n')
	s = s[1:]
	for i in s:
		update(i)

processInput('''4
CarriageBolt 45
Eyebolt 50
Washer 120
Rivet 10
CarriageBolt 45
Eyebolt 45
Washer 140
Rivet 10''')
printChanges()
clear()
print ''
processInput('''3
2DNail 3
4DNail 5
8DNail 10
8DNail 11
4DNail 5
2DNail 2''')
printChanges()
clear()