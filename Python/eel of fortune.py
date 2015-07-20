import re

def problem(word, offender):
	return re.sub('[^' + offender + ']', '', word) == offender
	
print problem('synchronized', 'snond')
print problem('misfunctioned', 'snond')
print problem('mispronounced', 'snond')
print problem('shotgunned', 'snond')
print problem('snond', 'snond')
