"""
Given integers in a square  matrix. First sort the matrix by frequency. For the
integers that have same frequency, sort them by order.

Populate the matrix from left bottom towards right top starting from the
bottom right corner.
"""

from collections import defaultdict 
def sort_matrix(m):
    row_len, col_len = len(m), len(m[0])
    counter = defaultdict(int)
    for i in range(row_len):
        for j in range(col_len):
            counter[m[i][j]] += 1

    count_key_list = [(count, key) for key, count in counter.items()]
    count_key_list.sort()

    sorted_m = [[] for _ in range(row_len)]
    # populaten the matrix with sorted integers
    # first go diagonally through elements starting from top row.
    count, value = count_key_list.pop()
    for i in range(col_len):
        row, col = 0, i
        while col >= 0:
            sorted_m[row].append(value)
            # Update row and col index accordingly
            row += 1
            col -= 1
            # Update count and see if the value is all used up.
            count -= 1
            if count == 0:
                count, value = count_key_list.pop()
        
    # go diagonally through elements starting from right most column
    for i in range(1, row_len):
        row, col = i, col_len-1
        # This forms lower traingular matrix as such the loop condition will
        # be to check if row index goes out of index.
        while row < row_len:
            sorted_m[row].append(value)
            # Update row and col index accordingly
            row += 1
            col -= 1
            count -= 1
            if count == 0 and count_key_list:
                count, value = count_key_list.pop()

    print(sorted_m)
    return sorted_m


matrix = [
        [3, 1, 1],
        [-2, 3, -2],
        [4, 3, 4]
        ]
sort_matrix(matrix)

