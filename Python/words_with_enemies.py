



def fire(one, two):
	for i in one:
		if i in one and i in two:
			one = one.replace(i, '', 1)
			two = two.replace(i, '', 1)
	print one, ' | ', two
	if len(one) > len(two):
		print "Left side wins."
	elif len(two) > len(one):
		print "Right side wins."
	else:
		print "It's a tie."

fire('hat','cat')
fire('miss', 'hiss')
fire('because','cause')
fire('hello','below')
fire('hit','miss')
fire('rekt','pwn')
fire('combo','jumbo')
fire('critical','optical')
fire('isoenzyme','apoenzyme')
fire('tribesman','brainstem')
fire('blames','nimble')
fire('yakuza','wizard')
fire('longbow','blowup')
