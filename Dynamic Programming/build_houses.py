'''
build a row of N houses that can be of K different colors
minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the
nth house with kth color, return the minimum cost which achieves this goal.
'''

'''
Solution1:
Using dynamic programming
Find the min cost using each color of house n and store it.
Now for each color of house n + 1, get the min of cost of painting with other colors.
You already have the answer for that subproblem.

The problem with this solution is that we have a for loop inside the second for loop
that checks the minimum cost of coloring the previous house without taking into account
the cost of painting previous house with the color the house is being painted with.
makes the runtime O(n^3) 
'''
def min_cost_build_houses(color_cost):
    num_houses = len(color_cost)
    num_colors = len(color_cost[0])
    build_cost = [[0]*num_colors for _ in range(num_colors)]
    build_cost[0] = color_cost[0]

    for i in range(1, num_houses):
        for j in range(num_colors):
            min_cost = float("inf")
            for k in range(num_colors):
                if j == k:
                    continue
                min_cost = min(min_cost, build_cost[i-1][k])
            build_cost[i][j] = min_cost + color_cost[i][j]
    return min(build_cost[-1])

arr = [
      [1, 3, 2, 1, 4]
    , [2, 1, 5, 2, 1]
    , [4, 1, 3, 3, 2]
    , [1, 1, 1, 1, 1]
    , [2, 5, 2, 4, 1]
]

'''
Solution 2:
Could use solution 1
and simple store the highest minimum cost and the second highest minimum cost
along with the colors with those values
'''
print(min_cost_build_houses(arr))

