"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):
1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

Note:
    The matrix is mxn.
    There is always two or more people.
"""

# This can be solved by finding the median of x and y axis.

def min_total_distance_to_meeting_point(grid):
    min_total_distance = 0
    x_coordinates, y_coordinates = [], []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                x_coordinates.append(i)
                y_coordinates.append(j)

    # Find the median of x and y coordinates
    median_of_x_coordinate = x_coordinates[len(x_coordinates)//2]
    # y_coordinates need to be sorted to find the median.
    y_coordinates.sort()
    median_of_y_coordinate = y_coordinates[len(y_coordinates)//2]

    # Find the total distance
    for m, n in zip(x_coordinates, y_coordinates):
        min_total_distance += abs(
                m - median_of_x_coordinate) + abs(n - median_of_y_coordinate)

    return min_total_distance

assert min_total_distance_to_meeting_point([
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]]) is 6
