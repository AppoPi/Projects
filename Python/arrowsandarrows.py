# import pprint
# pp = pprint.PrettyPrinter(indent=4)
import sys
import ctypes

#START PRINT COLOR
# Constants from the Windows API
STD_OUTPUT_HANDLE = -11
FOREGROUND_RED    = 0x0004 # text color contains red.

def get_csbi_attributes(handle):
    # Based on IPython's winconsole.py, written by Alexander Belchenko
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    return wattr


handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)
ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
#END PRINT COLOR



input = '''
^^v>>v^>>v<<<v>v<>>>>>>>>^vvv^^vvvv<v^^><^^v>
>><<>vv<><<<^><^<^v^^<vv>>^v<v^vv^^v<><^>><v<
vv<^v<v<v<vvv>v<v<vv<^<v<<<<<<<<^<><>^><^v>>>
<v<v^^<v<>v<>v<v<^v^>^<^<<v>^v><^v^>>^^^<><^v
^>>>^v^v^<>>vvv>v^^<^<<<><>v>>^v<^^<>v>>v<v>^
^^^<<^<^>>^v>>>>><>>^v<^^^<^^v^v<^<v^><<^<<<>
v<>v^vv^v<><^>v^vv>^^v^<>v^^^>^>vv<^<<v^<<>^v
<<<<<^<vv<^><>^^>>>^^^^<^<^v^><^v^v>^vvv>^v^^
<<v^<v<<^^v<>v>v^<<<<<>^^v<v^>>>v^><v^v<v^^^<
^^>>^<vv<vv<>v^<^<^^><><^vvvv<<v<^<<^>^>vv^<v
^^v^>>^>^<vv^^<>>^^v>v>>v>>v^vv<vv^>><>>v<<>>
^v<^v<v>^^<>>^>^>^^v>v<<<<<>><><^v<^^v><v>^<<
v>v<><^v<<^^<^>v>^><^><v^><v^^^>><^^<^vv^^^>^
v><>^><vv^v^^>><>^<^v<^><v>^v^<^<>>^<^vv<v>^v
><^<v>>v>^<<^>^<^^>v^^v<>>v><<>v<<^><<>^>^v<v
>vv>^>^v><^^<v^>^>v<^v><>vv>v<^><<<<v^<^vv<>v
<><<^^>>^<>vv><^^<vv<<^v^v^<^^^^vv<<>^<vvv^vv
>v<<v^><v<^^><^v^<<<>^<<vvvv^^^v<<v>vv>^>>^<>
^^^^<^<>^^vvv>v^<<>><^<<v>^<<v>>><>>><<^^>vv>
<^<^<>vvv^v><<<vvv<>>>>^<<<^vvv>^<<<^vv>v^><^
'''

length = 45
height = 20
form = []

#translate string into 2d list
for i in input.split('\n'):
	if list(i) != []:
		form.append(list(i))

#return direction, new x, new y
def next(x, y):
	dir = form[y][x]
	if dir == '^':
		y -= 1
	elif dir == 'v':
		y += 1
	elif dir == '<':
		x -= 1
	elif dir == '>':
		x += 1
	
	x %= length
	y %= height
	
	return form[y][x], x, y

#initialize max cycle length as 0
#and list to hold cycle coordinates
maxCycleLength = 0
maxStack = []

#loop through graph
for y in range(height):
	for x in range(length):
		#Start with an empty stack at length 0 for longest cycle
		stack = []
		count = 0
		
		#Continue while next vertex does not exist in graph
		while (x,y) not in stack:
			#Add each encountered vertex to graph
			stack.append((x,y))
			symbol, x, y = next(x,y)
		
		#Backtrack to isolate cycle
		tempStack = []
		while True:
			if len(stack) > 0:
				temp = stack.pop()
			if not temp == (x,y):
				tempStack.append(temp)
				#Count cycle length
				count += 1
			else:
				tempStack.append((x,y))
				break
		
		#Check if last cycle found is longer than recorded "max cycle"
		if count > maxCycleLength:
			maxCycleLength = count
			maxStack = tempStack
#print given
print input
#print found length
print maxCycleLength
# print maxStack

#print max cycle highlighted graph
try:
	for y in range(height):
		for x in range(length):
			if (x,y) in maxStack:
				ctypes.windll.kernel32.SetConsoleTextAttribute(handle, FOREGROUND_RED)
			else:
				ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
			
			sys.stdout.write(form[y][x])
		sys.stdout.write('\n')
except:
	print sys.exc_info()[0]
finally:
	ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)