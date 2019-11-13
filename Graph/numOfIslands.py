# the logic is right 
# just remove thhat namedtuple completely and simply use i, j instead

# Given a grid with 1 and 0, you are supposed to return the number of 
# groups of connected 1s

# TODO(henxing): Fix this
import collections
Coordinate = collections.namedtuple("row", "col")

def numOfIslands(grid):
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == "1":
				dfs(grid, Coordinate(i, j))
				count += 1
	return count

def dfs(grid, pt):
	if (pt.row < 0 or pt.row >= len(grid)) or (pt.col < 0 or pt.col >= len(grid[0])) or grid[pt.row][pt.col] == "0":
		return
	dfs(grid, Coordinate(pt.row-1, pt.col))
	dfs(grid, Coordinate(pt.row+1, pt.col))
	dfs(grid, Coordinate(pt.row, pt.col-1))
	dfs(grid, Coordinate(pt.row, pt.col+1))

grid =  [
	  ['1','1','1','1','0']
	, ['1','1','0','0','0']
	, ['1','1','0','1','0']
	, ['1','1','0','1','0']
	]
print(numOfIslands(grid))

