import sys

# single line comment

""" this is a multiline comment
  which spawns many lines
"""

var1 = 0
var2 = 1

if not sys.argv[1:]:
	num = int(input('Enter an integer: '))
else:
	num = int(sys.argv[1])
	
count = 0

while(count<num):
	var1, var2 = var2, var1 + var2
	print(str(var2) + ",", end=" ")
	count = count  + 1