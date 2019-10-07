"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].


The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

from collections import defaultdict
from collections import deque

def calc_equation(equations, values, queries):
    graph = defaultdict(list)
    # create graph from the list of equations
    for eqn, value  in zip(equations, values):
        x, y = eqn
        graph[x].append((y, value))
        graph[y].append((x, 1/value))

    # for each query, do bfs in graph to compute the result.
    result = [compute_result(x, y, graph) for x, y in queries]
    return result

def compute_result(x, y, graph):
    """Computes the value of x/y using relations denoted by graph."""
    if x not in graph or y not in graph:
        return -1

    queue = deque([(x, 1)]) # Holds the variable name and value of x/variable
    visited = set() # Keeps track of already visited nodes to avoid infinite loop
    # Since the input is always valid, this loop should end at some point with
    # the if condition inside it.
    while queue:
        node, val = queue.popleft()
        # Return the val (x/y) if the variable is y
        if node == y:
            return val
        for neighbor, neighbor_val in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, val * neighbor_val))
        visited.add(node)
    return -1

equations = [['a', 'b'], ['b', 'c']]
values = [2.0, 3.0]
queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]

assert calc_equation(equations, values, queries) == [6, 0.5, -1, 1, -1]

equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

assert calc_equation(equations, values, queries) == [-1, -1, 1, 1]
