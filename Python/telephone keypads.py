import re

file = 'brit-a-z.txt'
wordlist = []
with open(file) as f:
	wordlist = f.read().split('\n')


def telephone(input):
	input += ' '
	numbers = re.findall("[0-9]+ ", input )
	dict = {'0 ':'', '1 ':'', '2 ':'a', '22 ':'b', '222 ':'c', '3 ':'d', '33 ':'e','333 ':'f',
	 '4 ':'g', '44 ':'h', '444 ':'i', '5 ':'j', '55 ':'k', '555 ':'l', '6 ':'m', '66 ':'n',
	 '666 ':'o','7 ':'p', '77 ':'q', '777 ':'r', '7777 ':'s', '8 ': 't', '88 ':'u', '888 ':'v',
	 '9 ':'w', '99 ':'x', '999 ':'y', '9999 ':'z'}

	s = ''
	for i in numbers:
		s += dict[i]
	return s

def startsWith(pre):
	for i in wordlist:
		if i.startswith(pre):
			print i
	
startsWith(telephone('7777 666 555 3'))