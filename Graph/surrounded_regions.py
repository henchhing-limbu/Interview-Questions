# TODO(henxing): Not working; Finish this
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:
"""

def solve(board):
    visited = {} # keeps track of visited region
    # go through each region and capture if the regions are capturable
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O' and board[i][j] not in visited:
                capture_region(i, j, board, visited)

def capture_region(i, j, board, visited):
    """Capture regions surrounded by 'X' if possible."""
    # Region 'O' can't be captured if it's in the wall.
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False

    # Region is already visited; return it's value
    if (i, j) in visited:
        return visited[(i, j)]

    # Mark this region as visited
    visited.add((i, j))
    
    is_capturable = True
    # Check all the region's adjacent regions make it possible to capture.
    for x, y in ((i, j-1), (i, j+1), (i+1, j)):
        if (x, y) not in visited:
            is_capturable = is_capturable and capture_region(x, y, board, visited)

    # Capture the region as it's connecting region are capturable as well.
    if is_capturable:
        board[i][j] = 'X'
    return is_capturable


board1 = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
        ]
solve(board1)

board2 = [
        ["X","O","X","X"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"]
        ]
solve(board2)

board3 = [
        ["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]
        ]

solve(board3)
new_board3 = [
        ["O","O","O","O","X","X"],
        ["O","O","O","O","O","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","X","O"],
        ["O","X","O","X","O","O"],
        ["O","X","O","O","O","O"]
        ]
assert board3 == new_board3

board4 = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
        ]
solve(board4)
print(board4)
new_board4 = [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
        ]


