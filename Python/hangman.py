import random

wrongs = 0
guesses = []

def getLines(file):
	#Open file
    with open(file) as f:
		#Read through lines
        for i, l in enumerate(f):
            pass
	#Return lines
    return i + 1

def generateWord(file):
	#Read from file
	f = open(file,'r')
	#Generate random number (0-lines)
	l = random.randrange(0,getLines(file))
	word = "default"
	#Read nth line into word
	for i in range(l):
		word = f.readline()
	#Return generated word
	return word.rstrip()

def generate(file, diff):
	word = "default"
	min = 6
	max = 10
	if diff == 'e':
			min = 9
	elif diff == 'm':
			min = 6
			max = 8
	elif diff == 'h':
			max = 6
	while True:
		word = generateWord(file)
		if len(word) >= min and len(word) <= max:
			return word

def drawHangman(num):
	#Predrawn hangman
	man = """
	2222
	1  3
	1 546
	1  4
	1 7 8
	1
	"""
	for i in man:
		#Draw spaces and tabs
		if i in "\t\n ":
			print i,
		#Draw hangman
		elif i in "12345678":
			if i <= str(num):
				print i,
			else:
				print " ",
	print ""

# Generate secret word
# secret = generate('wordlist.txt','e')
# Initialize board
# reveal = [False] * (len(secret)-1)


def drawBoard(num):
	#Draw board
	for i in range(len(secret)):
		#Revealed
		if reveal[i]:
			print " " + secret[i] + " ",
		#Hidden
		else:
			print " _ ",
	print ""

def guess(c):
	#Already guessed
	if c in guesses:
		print "You've already incorrectly guessed ", c, "."
		return False
	elif secret.find(c) > 0 and reveal[secret.find(c)]:
		print "You've already correctly guessed", c + "."
		return False
	global wrongs
	#Correct
	if c in secret:
		for i in range(len(secret)):
			if c == secret[i]:
				reveal[i] = True
		return True
	#Incorrect
	else:
		wrongs += 1
		guesses.append(c)
		return False

#Request difficulty
while True:
	diff = raw_input("Enter difficulty[E,M,H]:")
	if len(diff)==1 and diff in "EMHemh":
		diff = diff.lower()
		break

#Generate secret word
secret = generate('wordlist.txt', diff)
#Initialize board
reveal = [False] * (len(secret))

while True:
	#Print information
	drawHangman(wrongs)
	drawBoard(wrongs)
	print guesses
	print secret
	
	if wrongs > 7:
		#Lose
		print "Sorry, you lost. Your word was " + secret.upper() + ". Please try again"
		break;
	elif False not in reveal:
		#Win
		print "Yes. That's right!. " + secret.upper() + ". Congratulations, you've guessed it!"
		break
	#Guess
	while True:
		input = raw_input("Guess a letter: ").lower()
		#"Validate"
		if len(input) == 1 and input.isalpha():
			break
	guess(input)



