import sys
import re

with open("C:\users\mbuser\Desktop\Three.txt", 'r') as file:
	text = file.read()

pa = "[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]"
regex = re.compile(pa)
r = regex.search(text)
results = regex.findall(text)
word = ''
for i in results:
	word += i[4]

print word