"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

def min_path_sum(grid):
	if not grid or not grid[0]:
		return 0
	row, col = len(grid), len(grid[0])
	# Update the last row. They don't have option to choose
	for i in range(col - 2, -1, -1):
		grid[row-1][i] += grid[row-1][i+1]
	# Update the last column. They don't have option to choose
	for i in range(row - 2, -1, -1):
		grid[i][col-1] += grid[i+1][col-1]
	
	# go through remaining position in the grid and choose min from down or
	# cell sum.
	for i in range(row - 2, -1, -1):
		for j in range(col - 2, -1, -1):
			grid[i][j] += min(grid[i+1][j], grid[i][j+1])
	return grid[0][0]

print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
