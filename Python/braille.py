braille = ['''O. O. O. O. O. .O O. O. O. OO
OO .O O. O. .O OO .O OO O. .O
.. .. O. O. O. .O O. O. O. ..''',
'''O. OO O. .O O. OO .O OO O. OO O. .O O. O. O. O. OO .O OO O. O.
.. .O .. OO .O .. O. .. .O O. .. OO OO .O O. .O OO O. .. .. O.
.. O. .. O. O. O. .. .. O. O. .. O. .. O. O. O. .. .. .. .. O.''',
'''O. OO .O .O OO O. .O O. O. .O O. O. .O .O .O .O OO O. O. O. OO
.. .O OO O. .. .. OO .O OO O. .. O. O. O. OO O. .. .. O. O. .O
.. O. O. .. O. .. O. .. O. .. .. O. .. O. O. .. .. .. O. O. OO''',
'''O. OO .O .O O. .O .O O. .O .O O. O. .O O. OO .O .O OO
.. .O OO O. .. OO O. O. O. OO .. OO O. .. .O O. O. ..
.. O. O. .. OO O. .. O. .. O. .. O. .. .. O. .. O. O.''',
'''O. O. O. O. .O OO OO .O O. .O OO O. O. O. .O O. O. .O .O O. OO
.O O. .O OO O. .O .O O. O. O. .O .. .. O. O. .O .. OO O. .O .O
O. OO .. O. .. O. .. .. OO .. .. OO .. O. .. OO .. O. .. O. O.''',
'''OO O. OO OO O. .O O. O. OO OO O. O. OO OO OO O. OO .O OO O. O. O. OO
.. .. OO .O .O OO .O OO .O .O OO .O .O .O .O .. .. O. .. .. O. O. .O
O. .. .. O. .. O. O. .. OO .. O. O. .. OO O. .. O. .. .. .. O. O. OO'''
]

brailleDict = {
'O.....':'a',
'O.O...':'b',
'OO....':'c',
'OO.O..':'d',
'O..O..':'e',
'OOO...':'f',
'OOOO..':'g',
'O.OO..':'h',
'.OO...':'i',
'.OOO..':'j',
'O...O.':'k',
'O.O.O.':'l',
'OO..O.':'m',
'OO.OO.':'n',
'O..OO.':'o',
'OOO.O.':'p',
'OOOOO.':'q',
'O.OOO.':'r',
'.OO.O.':'s',
'.OOOO.':'t',
'O...OO':'u',
'O.O.OO':'v',
'.OOO.O':'w',
'OO..OO':'x',
'OO.OOO':'y',
'O..OOO':'z'
}

stringDict = {
'a':'O.....',
'b':'O.O...',
'c':'OO....',
'd':'OO.O..',
'e':'O..O..',
'f':'OOO...',
'g':'OOOO..',
'h':'O.OO..',
'i':'.OO...',
'j':'.OOO..',
'k':'O...O.',
'l':'O.O.O.',
'm':'OO..O.',
'n':'OO.OO.',
'o':'O..OO.',
'p':'OOO.O.',
'q':'OOOOO.',
'r':'O.OOO.',
's':'.OO.O.',
't':'.OOOO.',
'u':'O...OO',
'v':'O.O.OO',
'w':'.OOO.O',
'x':'OO..OO',
'y':'OO.OOO',
'z':'O..OOO'
}

def brailledToString(b):
	line_len = len(b) / 3
	list = []
	string = ''
	for i in range(0, len(b)/3, 3):
		string += brailleDict[b[i : i + 2] + b[i + line_len + 1 : i + 2 + line_len + 1] + b[i + 2 * line_len + 2 : i + 2 + 2 * line_len + 2]]
	return string

def stringToBraile(b):
	line1 = line2 = line3 =''
	for i in b:
		line1 += stringDict[i][0:2] + ' '
		line2 += stringDict[i][2:4] + ' '
		line3 += stringDict[i][4:6] + ' '
	return line1 + '\n' + line2 + '\n' + line3

for i in braille:
	print brailledToString(i)
	print stringToBraile(brailledToString(i))

print 