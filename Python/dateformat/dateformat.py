import re
import sys
import os

def reformat(date):
	day, month, year = 0, 0, 0
	
	#Case 1 yyyy-mm-dd
	if re.match(ur'[1-2][0-9][0-9][0-9]-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])', date, flags=0):
		year = int(date[0:4])
		month = int(date[5:7])
		day = int(date[8:10])
	
	#Case 2 mm/dd/yy
	elif re.match(ur'(0[1-9]|1[0-2])/([0-2][0-9]|3[0-1])/[0-9][0-9]', date, flags=0):
		month = int(date[0:2])
		day = int(date[3:5])
		year = int("19" + date[6:8])
		if year < 1950:
			year += 100
	
	#Case 3 mm#yy#dd
	elif re.match(ur'(0[1-9]|1[0-2])\#[0-9][0-9]\#([0-2][0-9]|3[0-1])', date, flags=0):
		month = int(date[0:2])
		day = int(date[6:8])
		year = int("19" + date[3:5])
		if year < 1950:
			year += 100
	
	#Case 4 dd*mm*yyyy
	elif re.match(ur'([0-2][0-9]|[3][0-1])\*(0[0-9]|1[0-2])\*[1-2][0-9][0-9][0-9]', date, flags=0):
		day = int(date[0:2])
		month = int(date[3:5])
		year = int(date[6:10])
	
	#Case 5(month word) dd, yy
	elif re.match(ur'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-2][0-9]|3[0-1]), [0-9][0-9]\b', date, flags=0):
		months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
		month = int(months.index(date[0:3])) + 1
		day = int(date[4:6])
		year = int(date[8:])
		if year < 50:
			year += 2000
		elif year > 49:
			year += 1900
	
	#Case 6 (month word) dd, yyyy
	elif re.match(ur'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([0-2][0-9]|3[0-1]), [0-9][0-9][0-9][0-9]\b', date, flags=0):
		months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
		month = int(months.index(date[0:3])) + 1
		day = int(date[4:6])
		year = int(date[8:])		
	
	return '%02d-%02d-%02d' % (year, month, day)


if len(sys.argv) != 3:
	print "Enter filename for input and output."
	sys.exit()

with open(sys.argv[1]) as f:
	content = f.readlines()
	content =  [x.strip('\n') for x in content]


f = open(sys.argv[2], 'w')


for i,j in enumerate(content):
	f.write(reformat(content[i])+ '\n')

