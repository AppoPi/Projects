
# def carry_adding(one, two):
	# width = max(len(str(one)),len(str(two)))+1
	# print str(one).rjust(width)
	# print '+' + str(two).rjust(width-1)
	# print '-' * width
	# print str(one + two).rjust(width)
	# print ""

def add(input):
	s = input.split('+')
	command = 'carry_adding('
	for i in s:
		command += str(i) + ', '
	exec( command[:-2] + ')' )

def carry_adding(*add):
	sum = 0
	for i in range(len(add)):
		sum += add[i]
	width = len(str(sum))+1
	for i in range(len(add)):
		if i == len(add)-1:
			print '+' + str(add[i]).rjust(width - 1)
		else:
			print str(add[i]).rjust(width)
	bar = '-' * width
	
	print bar
	print str(sum).rjust(width)
	print bar
	
	# initialize output string
	carries = ' '
	# convert numbers from int to string, standardize length of numbers
	add = [str(str(i).zfill(width-1)) for i in add]
	# initialize last carried digit
	last = 0
	for j in range(len(add[0])-1,0,-1): # for each digit
		# reset sum of j digit
		extra = 0
		for i in range(len(add)): # for each addend
			# sum the values
			extra += int(add[i][j])
		# add in the carried digit
		extra += last
		# take 10s digits and higher
		last = extra/10		
		# append to beginning of output string
		carries = (str(extra/10%10) if extra >= 10 else ' ') + carries
	print " " + carries
	print ''
	
add('23+9+66')
add('8765+305')
add('12+34+56+78+90')
add('999999+1')
