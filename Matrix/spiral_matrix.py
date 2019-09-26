def spiral_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    top, left, bottom, right = 0, 0, n-1, n-1

    num = 1
    while True: 
        # populate left to right
        for j in range(top, right+1):
            matrix[top][j] = num
            print(num)
            if num == n**2:
                return matrix
            num += 1
        top += 1

        # populate top to bottom
        for i in range(top, bottom+1):
            matrix[i][right] = num
            if num == n**2:
                return matrix
            num += 1
        right -= 1

        # populate right to left
        for j in range(right, left-1, -1):
            matrix[bottom][j] = num
            if num == n**2:
                return matrix
            num += 1
        bottom -= 1

        print('Reached here')
        # populate bottom to top
        for i in range(bottom, top-1, -1):
            matrix[i][left] = num
            if num == n**2:
                return matrix
            num += 1
        left += 1

    return matrix

spiral_matrix(2)
