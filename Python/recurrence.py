import re

def recurrence(pattern, first, n):
	print "Term 0: " + str(first)
	stack = re.findall(r'[*,/,+,-]-?[0-9]+', pattern)
	r = first
	for i in range(n):
		for j in range(len(stack)):
			# print "r = r " + str(stack[j])
			exec("r = r " + str(stack[j]))
		print "Term " + str(i+1) + ": " + str(r)

recurrence('*2 +1', 1, 10)
print "" 
recurrence('*-2', 1, 8)
print "" 
recurrence('+2 *3 -5', 0, 10)