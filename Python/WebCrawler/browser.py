import time
import subprocess


#Open website file
file = open("C:\users\mbuser\Desktop\websites.csv", 'r')


#Loop through million websites
for x in range(0,1000000):
	#Read in line from file
	webpage = file.readline()
	#Open Chrome to webpage
	p = subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe", webpage])
	#Wait 5 seconds
	time.sleep(5)
	#Kill browser
	p.kill()
	#End Loop