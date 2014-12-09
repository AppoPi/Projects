import time
import subprocess
import os.path
from os.path import expanduser

#Open website file
file = open("C:\users\mbuser\Desktop\websites.csv", 'r')


home = expanduser("~") + "\\Desktop\\"

try:
	x = 0;
	total = 1000000
	
	if os.path.isfile(home + "PythonDomainTestLog.txt"):
		log = open(home + "PythonDomainTestLog.txt", 'r')
		x = int(log.readline())
		for i in range(0, x):
			file.readline()
			total = total - 1
			
	
	#Loop through million websites
	while x < 1000000:
		#Read in line from file
		webpage = file.readline()
		#Open Chrome to webpage
		p = subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe", webpage])
		#Wait 5 seconds
		time.sleep(5)
		#Kill browser
		p.kill()
		#End Loop
		x = x + 1
	
except KeyboardInterrupt:
	print x
	log = home + "PythonDomainTestLog.txt"
	outstream = open(log, 'w+')
	outstream.write(str(x))