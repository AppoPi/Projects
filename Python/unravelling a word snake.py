
snake1 = '''6
SNAKE
    A   DUSTY
    T   N   U
    SALSA   M
            M
            YACHTS
'''

snake2 = '''8
W    DINOSAUR
I    E      E
Z  CAR  Y   A
A  I    L   C
R  D    T  OT
D  R    B  V
R  O    U  A
YAWN    SGEL
'''

snake3 = '''8
NUMEROUS
       Y
LUXURY M
O    E B
B O  A O
M DAOR L
Y      I
SDRATSUC
'''

snake4 = '''10
R       TIGER
E       O   E
S       H   T  SO
I  GRAPES   U  N
G  A        R  R
NULL  GNIHTON  E
      R        T
      A        N
      N        A
      DELIGHTFUL
'''

def longest(s):
	max = -1
	while s.find('\n') > 0:
		f = s.find('\n')
		s = s[f+1:]
		if f > max:
			max = f
	return max
	
def pad(s, long):
	s = s[s.find('\n')+1:]
	l = []
	while s.find('\n') > 0:
		f = s.find('\n')
		if s[:f].isalpha:
			l.append(list(s[:f].ljust(long, ' ')))
		s = s[f+1:]
	return l
	
def getWords(s, width, height):
	string = ''
	x, y = 0, 0
	nextLetter = s[x][y]
	curr = 'unknown'
	once = 'True'
	while(nextLetter != ' '):
		string += nextLetter
		s[x][y] = ' '
		last = curr
		curr = 'none'
		if x + 1 < height and s[x + 1][y].isalpha():
			x += 1
			curr = 'down'
		elif y + 1 < width and s[x][y + 1].isalpha():
			y += 1
			curr = 'right'
		elif x - 1 > -1 and s[x - 1][y].isalpha():
			x -= 1
			curr = 'up'
		elif y - 1 > -1 and s[x][y - 1].isalpha():
			y -= 1
			curr = 'left'
		nextLetter = s[x][y]
		if last != curr and not once:
			last = curr
			lastChar = string[-1:]
			string += ' ' + lastChar
		once = False
		# print string
	return string[:-2]

def unravel(snake):
	width = longest(snake)
	height = int(snake[:snake.find('\n')])
	snake = pad(snake, width)
	print getWords(snake, width, height)

	
unravel(snake1)
unravel(snake2)
unravel(snake3)
unravel(snake4)