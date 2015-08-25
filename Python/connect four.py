import re

class ConnectFour:
	size = 7
	fill = '.'
	a = [[fill] * size for i in range(size)]
	
	def __init__(self):
		self.a = [[self.fill] * self.size for i in range(self.size)]
		
	def printBoard(self):
		print '    a b c d e f g'
		print '6   {} {} {} {} {} {} {}'.format(self.a[5][0], self.a[5][1], self.a[5][2], self.a[5][3], self.a[5][4], self.a[5][5], self.a[5][6])
		print '5   {} {} {} {} {} {} {}'.format(self.a[4][0], self.a[4][1], self.a[4][2], self.a[4][3], self.a[4][4], self.a[4][5], self.a[4][6])
		print '4   {} {} {} {} {} {} {}'.format(self.a[3][0], self.a[3][1], self.a[3][2], self.a[3][3], self.a[3][4], self.a[3][5], self.a[3][6])
		print '3   {} {} {} {} {} {} {}'.format(self.a[2][0], self.a[2][1], self.a[2][2], self.a[2][3], self.a[2][4], self.a[2][5], self.a[2][6])
		print '2   {} {} {} {} {} {} {}'.format(self.a[1][0], self.a[1][1], self.a[1][2], self.a[1][3], self.a[1][4], self.a[1][5], self.a[1][6])
		print '1   {} {} {} {} {} {} {}'.format(self.a[0][0], self.a[0][1], self.a[0][2], self.a[0][3], self.a[0][4], self.a[0][5], self.a[0][6])

	def drop(self, col, player):
		for i in range(0, self.size-1):
			if self.a[i][col] == self.fill:
				self.a[i][col] = player
				return True
		return False

	def winner(self):
		# Horizontal
		for i in range(len(self.a)):
			for j in range(len(self.a[0])-4):
				if self.a[i][j] == self.a[i][j+1] == self.a[i][j+2] == self.a[i][j+3] != self.fill:
					return self.a[i][j], i, j, i, j+1, i, j+2, i, j+3
		# Vertical
		for i in range(len(self.a)-4):
			for j in range(len(self.a)):
				if self.a[i][j] == self.a[i+1][j] == self.a[i+2][j] == self.a[i+3][j] != self.fill:
					return self.a[i][j], i, j, i+1, j, i+2, j, i+3, j
		# Diagonal /
		for i in range(3):
			for j in range(4):
				if self.a[i][j] == self.a[i+1][j+1] == self.a[i+2][j+2] == self.a[i+3][j+3] != self.fill:
					return self.a[i][j], i, j, i+1, j+1, i+2, j+2, i+3, j+3
		# Diagonal \
		for i in range(3,self.size):
			for j in range(4):
				if self.a[i][j] == self.a[i-1][j+1] == self.a[i-2][j+2] == self.a[i-3][j+3] != self.fill:
					return self.a[i][j], i, j, i-1, j+1, i-2, j+2, i-3, j+3
		return None

	def move(self, s):
		if s.isupper():
			xcol = ord(s) - ord('A')
			self.drop(xcol, 'X')
		elif s.islower():
			ocol = ord(s) - ord('a')
			self.drop(ocol, 'O')
		return False

	def interpretWinner(self, win, move):
		if win:
			s = win[0]
			return '{} won at move {} (with {}{} {}{} {}{} {}{})'.format(win[0], move,
				chr(ord('A') + win[2]), win[1] + 1,
				chr(ord('A') + win[4]), win[3] + 1,
				chr(ord('A') + win[6]), win[5] + 1,
				chr(ord('A') + win[8]), win[7] + 1)
		return None


horizontal = '''C  d
D  d
D  b
C  f
C  c
B  a
A  d
G  e
E  g'''

diagonal_up_right = '''D  d
D  c
C  c    
C  c
G  f
F  d
F  f
D  f
A  a
E  b
E  e
B  g
G  g
B  a'''

vertical = '''D a
D  a
D  a
D  a
D  d
D  c
C  c    
C  c
F  f
F  d
F  a
G  a
A  a
E  b
E  e
B  g
G  g
B  a'''

diagonal_up_left = '''A  a
A  e
A  e
A  e
B  b
B  c
C  E
D  e'''
pls = [horizontal, vertical, diagonal_up_right, diagonal_up_left]

for i in pls:
	c4 = ConnectFour()
	count = 1
	gameover = False
	for j in i:
		for i in re.findall('[A-z]', j):
			if not gameover:
				c4.move(i)
				if c4.winner():
					print c4.interpretWinner(c4.winner(), (count+1)/2)
					gameover = True
				count +=1
	c4.printBoard()
	print ''
	
