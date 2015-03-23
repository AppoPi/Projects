import time
import sys
from selenium import webdriver

import socket
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoAlertPresentException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait


#Open website file
file = open('websites.csv', 'r')

if len(sys.argv) != 2:
	print 'Error: browser unselected. firefox/chrome\nProper use: browser.py chrome OR browser.py firefox'
	sys.exit()

b = str(sys.argv[1])#raw_input('firefox/chrome/ie?: ')

if lower(b) == 'firefox':
	driver = webdriver.Firefox()
elif lower(b) == 'chrome':
	driver = webdriver.Chrome()
else: 
	print 'Error: invalid browser selected.'
	sys.exit()

driver.set_page_load_timeout(30)

#Loop through million websites
for x in range(0,1000000):
	#Read in line from file
	webpage = file.readline()
	try:
		#Open Chrome to webpage
		driver.get('http://' + webpage)
		time.sleep(2)
		if ec.alert_is_present:
			driver.switch_to_alert().dismiss()
	except NoAlertPresentException:
		pass
	except Exception as e:
		# Print
		print str(x) + ': http://' + str(webpage)
		print str(e)
	
	#End Loop