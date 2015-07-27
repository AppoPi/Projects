
def printBool(s):
	if s:
		print '|%-12s' % str(s) + '| True  |'
	else:
		print '|%-12s' % str(s) + '| False |'
print '----------------------'
print '|Expression  | Bool  |'
printBool('Hello World!')
printBool('')
printBool('0')
printBool(1)
printBool(0)
printBool(0.0)
printBool([])
printBool([1,2,3])
printBool(True)
printBool(False)
print '----------------------'