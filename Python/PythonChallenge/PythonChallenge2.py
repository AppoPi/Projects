import sys
from sets import Set

with open("C:\users\mbuser\Desktop\longtext.txt", 'r') as file:
	data = file.readlines()[0]

str = ""
for i in range(len(data)):
	if data[i] in 'abcdefghijklmnopqrstuvwxyz':
		str += data[i]

print str