import os
import sys
from os.path import expanduser
import subprocess
import platform
from _winreg import *

################DETERMINE MBAM PATH
mbampath = ""
osbit = 0 

if os.path.isdir("C:\Program Files (x86)\Malwarebytes' Anti-Malware\\"):
	mbampath = "C:\Program Files (x86)\Malwarebytes' Anti-Malware\\"
	print "Using Program Files (x86)"
	osbit = 64
else:
	mbampath = "C:\Program Files\Malwarebytes' Anti-Malware\\"
	print "Using Program Files"
	osbit = 32

################RUN PROTECTION DRIVER
#os.chdir(mbampath + "\Chameleon\\")
#subprocess.call(['mbam-chameleon.exe','/o','/boot'])

################DELETE REGISTRY KEY
print "Testing registry key:\t\t",

if osbit == 32:
	#On x86 OS, delete  value "1" from:  KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce 
	key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce', 0, KEY_ALL_ACCESS)
else:
	#On x64 OS, delete value "1" from:   HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce
	key = OpenKey(HKEY_LOCAL_MACHINE, r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\RunOnce', 0, KEY_ALL_ACCESS)

DeleteValue(key,"1")
CloseKey(key)


################RENAME FILE TEST
os.chdir(mbampath)
print "Testing file rename:\t\t",
try:
	filename = "mbam.exe"
	os.rename(filename,"taco.exe")
	print "Failure"
	os.rename("taco.exe",filename)
except:
	print "Success"
	
################CREATE FOLDER TEST
os.chdir(mbampath + "\Chameleon\\")
print "Testing directory creation:\t",
try:
	if not os.path.isdir("TEST"):
		os.mkdir("TEST")
		print "Failure"
		try:
			os.rmdir("TEST")
		except:
			print "\t\t\t\tDirectory could not be removed"
	else:
		print "Directory already exists"
		try:
			os.rmdir("TEST")
		except:
			print "\t\t\t\tDirectory could not be removed"
except:
	print "Success"

################PROGRAMDATA TEST
print "Testing ProgramData creation: \t",
os.chdir("C:\ProgramData\Malwarebytes\Malwarebytes' Anti-Malware\\")
filename = "TEST.TXT"
try:
	if not os.path.exists(filename):
		file = open(filename,'w')
		file.write('')
		file.close()
		print "Failure"
		os.remove(filename)
	else:
		print "File already exists"
		#os.remove(filename)
except:
	print "Success"
	
################REMOVE PROTECTION DRIVER

os.chdir(mbampath + "\Chameleon\\")
subprocess.call(['mbam-chameleon.exe','/r'])


################REMOVE TEST DIRECTORY FROM CHAMELEON 
try:
	os.chdir(mbampath + "\Chameleon\\")
	os.rmdir("TEST")
	print "Chameleon directory cleanup:\t Success"
except:
	pass