import sys

class Item():
	def __init__(self, n, c):
		self.name = n
		self.categories = []
		for i in c:
			self.categories.append(i)

class List:
	list = []
	
	def addItem(self, *args):
		args = list(args)
		# Check for dupes by name
		for i in self.list:
			if i.name == args[0]:
				return
		self.list.append(Item(args[0], args[1:]))
	
	def printList(self, *args):
		if len(args) == 0:
			for i in self.list:
				sys.stdout.write('Title: ')
				sys.stdout.write(i.name + '\n')
				sys.stdout.write('Category: ')
				for j in i.categories:
					sys.stdout.write(str(j) + ' ')
				sys.stdout.write('\n')
		else:
			s = '----'
			for i in range(len(args)):
				s += args[i].upper()
				s += ' & '
			s = s[:-3]
			s += '----'
			print s
			for i in self.list:
				if sorted(i.categories) == sorted(args):
					print '- '  + i.name
	
	def saveList(self, file):
		s = ''
		with open(file, 'w') as f:
			for i in self.list:
				s += i.name
				s += '|'
				for j in i.categories:
					s += j
					s += '|'
				s.replace('\n','')
				s = s[:-1]
				s += '\n'
			f.write(s)
	
	def loadList(self, file):
		with open(file, 'r') as f:
			for line in f:
				title = line[:line.find('|')]
				cat = line[line.find('|')+1:].replace('\n','').split('|')
				self.addItem(title, cat)
	def printCategories(self):
		for i in self.list:
			print i.name + '|' + str(i.categories)
			# print type(i.categories)
x = List()
# x.loadList('out.txt')
x.addItem('A pixel is not a pixel is not a pixel' , 'Programming')
x.addItem('The Scheme Programming Language' , 'Programming')
x.addItem('Memory in C' , 'Programming')
x.addItem('Haskell\'s School of Music' , 'Programming', 'Music')
x.addItem('Algorithmic Symphonies from one line of code' , 'Programming', 'Music')
x.addItem('Modes in Folk Music' , 'Music')
x.addItem('The use of Melodic Minor Scales', 'Music')
# x.printCategories()
# x.printList()
x.printList('Music')
x.printList('Programming')
x.printList('Music', 'Programming')
# x.printList('Music', 'Programming', 'Art History')
# x.printList()
# x.saveList('out.txt')
# x.printList()
'''
A pixel is not a pixel is not a pixel|Programming
The Scheme Programming Language|Programming
Memory in C|Programming
Haskell's School of Music|Programming|Music
Algorithmic Symphonies from one line of code|Programming|Music
Modes in Folk Music|Music
The use of Melodic Minor Scales|Music
'''