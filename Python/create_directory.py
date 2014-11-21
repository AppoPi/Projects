import os
import sys

mbampath = ""

if os.path.isdir("C:\Program Files (x86)\Malwarebytes' Anti-Malware\Chameleon\\"):
	mbampath = "C:\Program Files (x86)\Malwarebytes' Anti-Malware\Chameleon\\"
elif os.path.isdir("C:\Program Files\Malwarebytes' Anti-Malware\Chameleon\\"):
	mbampath = "C:\Program Files\Malwarebytes' Anti-Malware\Chameleon\\"
else:
	print "MBAM could not be found, program terminated"
	sys.exit()
	
os.chdir(mbampath)
print "Testing directory creation:\t",
try:
	if not os.path.isdir("test"):
		os.mkdir("test")
		print "Directory successfully created"
	else:
		print "Directory already exists"
except:
	print "Directory could not be created"

print "Testing file creation:\t\t",
try:
	filename = "test.txt"
	if not os.path.exists(filename):
		file = open(filename,'w')
		file.write('Test 123')
		file.close()
		print "File successfully created"
	else:
		print "File already exists"
except:
	print "File could not be created"
	
print "Testing file rename:\t\t",
try:
	filename = "firefox.com"
	file = open(filename,'w')
	file.write('Test 123')
	file.close()
	print "File successfully overwritten"
except:
	print "file could not be overwritten"

