
import subprocess
import os

#kill MBAM if it's running
subprocess.Popen('taskkill /IM mbam.exe'.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

#copy license.conf to local directory
if os.path.isfile('%programdata%/Malwarebytes/Malwarebytes Anti-Malware/Configuration/license.conf'):
	subprocess.call('copy %programdata%/Malwarebytes/Malwarebytes Anti-Malware/Configuration/license.conf license.conf')
else:
	print "MBAM license.conf not found"
