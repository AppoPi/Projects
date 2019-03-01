import random

class Deck:
	deck = []
	def __init__(self):
		ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
		suits = [' of Hearts',' of Diamonds',' of Clubs',' of Spades']
		for i in range(4):
			for j in range(13):
				self.deck.append(ranks[j] + suits[i])
				
	def printDeck(self):
		for i in self.deck:
			print i
	
	def draw(self):
		return self.deck.pop()
	
	def shuffle(self):
		random.shuffle(self.deck)

d = Deck()
d.shuffle()
d.draw()
players = [[],[],[],[],[],[],[],[]]
numplayers = input("How many players (2-8)? ")

print ''

for i in range(numplayers):
	for j in range(2):
		players[i].append(d.draw())



for i in range(0, numplayers):
	if i== 0:
		print 'Your hand: ' + str(players[i][0]) + ', ' + str(players[i][1])
	print 'CPU ' + str(i + 1) + ': ' +  str(players[i][0]) + ', ' + str(players[i][1])

print ''
c = []

print '  Burn: ' + d.draw()

for i in range(3):
	c.append(d.draw())
print 'Flop: ' + c[0] + ', ' + c[1] + ', ' + c[2]
print '  Burn: ' + d.draw()
c.append(d.draw())
print 'Turn: ' + c[3]
print '  Burn: ' + d.draw()
c.append(d.draw())
print 'River: ' + c[4]