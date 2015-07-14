
def leftSum(word):
	sum = 0
	l = len(word)
	for i in word:
		sum += (ord(i) - ord('A') + 1) * l
		l -= 1
	return sum

def rightSum(word):
	sum = 0
	r = 1
	for i in word:
		sum += (ord(i) - ord('A') + 1) * r
		r += 1
	return sum

def balance(word):
	word = word.upper()
	for i in range(1, len(word)-1):
		left = word[:i]
		right = word[i+1:]
		lsum, rsum = leftSum(left), rightSum(right)
		if lsum == rsum:
			print left, word[i], right, '-', lsum
			return
	print word + " DOES NOT BALANCE"
words =["STEAD", "CONSUBSTANTIATION", "WRONGHEADED", "UNINTELLIGIBILITY", "BABE", "ABA", "SUPERGLUE"]

for w in words:
	balance(w)