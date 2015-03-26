import time
import sys
from selenium import webdriver
import socket
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait

import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Open website file
file = open('websites.csv', 'r')
b = ''
if len(sys.argv) != 2:
	#Default to chrome
	b = 'chrome'
else:
	b = str(sys.argv[1]).lower()#raw_input('firefox/chrome/ie?: ')

if b == 'firefox':
	# driver = webdriver.Firefox()
	print os.path.join('C:\\','Program Files (x86)','Mozilla Firefox','firefox.exe')
	binary = FirefoxBinary(os.path.join('C:\\','Program Files (x86)','Mozilla Firefox','firefox.exe'))
	
	driver = webdriver.Firefox(firefox_binary=binary)
elif b == 'chrome':
	driver = webdriver.Chrome()
else: 
	print 'Error: invalid browser selected.'
	sys.exit()

socket.setdefaulttimeout(5)
driver.set_page_load_timeout(5)
	
#Loop through million websites
for x in range(0,1000000):
	#Read in line from file
	webpage = 'http://' + file.readline()[:-1]
	try:
		print webpage
		#Open Chrome to webpage
		driver.get(webpage)
	except NoSuchWindowException and KeyboardInterrupt:
		sys.exit()
	except socket.timeout:
		print "Page load timeout"
		print "Timed out on " + webpage
		driver.close()
		driver = webdriver.Chrome()
	except Exception as e:
		print str(x) + ': http://' + webpage
		print str(e)
	if b == 'firefox':
		time.sleep(5)





























	# def waitForPageLoad(driver):
	# d = driver
	# d.implicitly_wait(2)        
	# loaded = False
	# for i in range(3):
		# try: 
			# el = d.find_element_by_tag_name("body")
			# loaded = True
			# break
		# except NoSuchElementException, e: 
			# print "crap"
		# finally:
			# d.implicitly_wait(3)
	# return loaded


