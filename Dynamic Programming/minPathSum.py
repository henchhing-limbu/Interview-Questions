
 CodePair
 henchhing 
No task has been added yet
Scratchpad
 
Question 1 


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
def minPathSum(a):
    if not a or not a[0]:
        return 0
    row, col = len(a), len(a[0])
    matrix = [[0] * col for _ in range(row)]
    
    while row > 0:
        row -= 1
        while col > 0:
            col -= 1
            matrix[row][col] = a[row][col] + getMinPath(matrix, row + 1, col + 1)
            print(matrix[row][col])
        col = len(a[0])
    return matrix[0][0]
            
            
def getMinPath(matrix, i, j):
    row, col = len(matrix), len(matrix[0])
    if i < row and j < col:
        return min(matrix[i][j-1], matrix[i-1][j])
    elif i >= row and j < col:
        return matrix[i-1][j]
    elif j >= col and i < row:
        return matrix[i][j-1]
    else:
        return 0
        
    
print(minPathSum([
]))
    

Stdin 
Stdout 
Run Code (⌥ + R)
Output:
0
 Chat
 
