"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


 Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

def oranges_rotting(grid):
    row_len, col_len = len(grid), len(grid[0])
    rotten_oranges = []
    # find rotten oranges
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 2:
                rotten_oranges.append((i, j))
    
    count = 0 # computes number of steps taken to rot oranges
    # do bfs
    while rotten_oranges:
        rotted_oranges = []
        for i, j in rotten_oranges:
            # rot the neighboring oranges if possible and keep track of them.
            for row, col in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
                if 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == 1:
                    grid[row][col] = 2
                    rotted_oranges.append((row, col))
        # Check if this rotten oranges were able to rot more
        # If so, just increment the count.
        if rotted_oranges:
            count += 1
        rotten_oranges = rotted_oranges
    if any(1 in row for row in grid):
        return -1
    return count

assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) is -1
assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) is 4
assert oranges_rotting([[0, 2]]) is 0
