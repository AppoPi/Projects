from  random import randrange
import pprint

p = pprint.PrettyPrinter(indent=4)

def generateGrid(sidelength, min, max):
	grid = [[randrange(min, max+1) for _ in range(sidelength)] for _ in range(sidelength)]
	return grid

def findShortest(grid, sidelength):
	cost = [[0 for _ in range(sidelength)] for _ in range(sidelength)]
	cost[0][0] = grid[0][0]
	for i in range(sidelength):
		for j in range(sidelength):
			if i==0 and j==0:
				cost[i][j] = grid[0][0]
			elif i==0:
				cost[i][j] = grid[i][j] + cost[i][j-1]
			elif j==0:
				cost[i][j] = grid[i][j] + cost[i-1][j]
			else:
				if cost[i][j-1] < cost[i-1][j]:
					cost[i][j] = grid[i][j] + cost[i][j-1]
				else:
					cost[i][j] = grid[i][j] + cost[i-1][j]
	return cost

sidelength = 5
low = 1
high = 3
grid = generateGrid(sidelength, low, high)
p.pprint(grid)
cost = findShortest(grid,sidelength)
print ""
p.pprint(cost)
print ""
print "The cost of the shortest path is "  + str(cost[sidelength-1][sidelength-1])

