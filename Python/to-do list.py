

class List:
	list = []
	
	def addItem(self, i):
		self.list.append(i)
	
	def deleteItem(self, i):
		self.list.remove(i)
	
	def viewList(self):
		for i in self.list:
			print i

x = List()
x.addItem('Take a shower')
x.addItem('Go to work')
x.viewList()

x.addItem('Buy a new phone')
x.deleteItem('Go to work')
x.viewList()