import sys

class Item():
	def __init__(self, n, c):
		self.name = n
		self.categories = c

class List:
	list = []
	
	def addItem(self, *args):
		# Check for dupes by name
		for i in self.list:
			if i.name == args[0]:
				return
		self.list.append(Item(args[0], args[1:]))
	
	def printList(self, *args):
		if len(args) == 0:
			for i in self.list:
				sys.stdout.write('Title: ')
				print i.name
				sys.stdout.write('Category: ')
				for j in i.categories:
					sys.stdout.write(str(j) + ' ')
				sys.stdout.write('\n')
			return
		elif len(args) == 1:
			print '---{0}---'.format(args[0].upper())
			for i in self.list:
				if args[0] in i.categories:
					print i.name
		elif len(args) == 2:
			print '---{0} & {1}---'.format(args[0].upper(), args[1].upper())
			for i in self.list:
				if sorted(i.categories) == sorted(args):
					print i.name
		# print ''
x = List()
x.addItem('A pixel is not a pixel is not a pixel' , 'Programming')
x.addItem('The Scheme Programming Language' , 'Programming')
x.addItem('Memory in C' , 'Programming')
x.addItem('Haskell\'s School of Music' , 'Programming', 'Music')
x.addItem('Algorithmic Symphonies from one line of code' , 'Programming', 'Music')
x.addItem('Modes in Folk Music' , 'Music')
x.addItem('The use of Melodic Minor Scales', 'Music')

x.printList()
x.printList('Music')
x.printList('Programming')
x.printList('Music', 'Programming')