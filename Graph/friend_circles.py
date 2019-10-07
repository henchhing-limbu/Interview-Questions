"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""

from collections import defaultdict
def find_circle_num(m):
    graph = defaultdict(list)
    # Create graph
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    count = 0
    visited = set() # keeps track of already visited nodes
    for node in graph:
        # If the node is not already visited, then dfs on it and find it's
        # friend circle.
        if node not in visited:
            stack = [node]  # Needed for dfs to keep track of visited items
            while stack:    # dfs
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in visited and neighbor != node:
                        stack.append(neighbor)
                visited.add(node)
            count += 1

    return count
            

assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 1, 1]]) == 1
assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert find_circle_num([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]) == 1
