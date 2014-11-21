import sys

menu = '1: Add a new contact\n2: Lookup a number\n3: Lookup a name\n-1: Quit\nUser Input: '
pb = {}
usr = int(input(menu))
while(usr != -1):
	if usr == 1:
		name = input('Please enter a contact\'s name: ')
		num = int(input('Please enter a contact\'s number: '))
		pb[name] = num
	elif usr == 2:
		name = input('Please enter a contact\'s name: ')
		if(name in pb):
			print(name + '\'s number is ' + str(pb[name]))
	elif usr == 3:
		num = int(input('Please enter a contact\'s number: '))
		found = False
		for key, value in pb.items():
			if value == num:
				print('The owner of the number \'' + str(value) + '\' is ' + key)
				found = True;
		if(not(found)):
			print('Contact could not be found')
	else
		print('Invalid input. Please try again')
	print()
	usr = int(input(menu))