"""In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
"""

import collections


def eventual_safe_nodes_dfs(graph):
    # Classic white-gray-black node representation in DFS algorithm
    WHITE, GRAY, BLACK = 0, 1, 2
    node_colors = collections.defaultdict(int)

    def dfs(node):
        # For a node that's not seen before, it must be already explored for
        # there not to be a cycle. If the node is not BLACK and is GRAY, it
        # means that there is a cycle in the graph.
        if node_colors[node] != WHITE:
            return node_colors[node] == BLACK

        # Currently exploring node, so it must be colored as GRAY.
        node_colors[node] = GRAY
        for neighbor in graph[node]:
            # If the subsequent nodes in dfs form a cycle, return False
            if not dfs(neighbor):
                return False

        # All neighbor nodes are explored. Color this node BLACK.
        node_colors[node] = BLACK
        return True
    return list(filter(dfs, range(len(graph))))


def eventual_safe_nodes_incoming_and_outgoing_edges(graph):
    safe_nodes = []
    # in_graph graph to keep track of nodes where the incoming edge is from.
    # out_graph to keep track of nodes where the outgoing edge is going to.
    in_graph, out_graph = collections.defaultdict(
            set), collections.defaultdict(set)

    for node, neighbors in enumerate(graph):
        out_graph[node] = set(neighbors)
        for neighbor in neighbors:
            in_graph[neighbor].add(node)

    # Find the nodes that don't have outgoing edges
    end_nodes = [node for node in out_graph if not out_graph[node]]
    
    queue = collections.deque(end_nodes)
    while queue:
        node = queue.popleft()
        # The nodes in queue are safe nodes.
        safe_nodes.append(node)

        # Remove the node from it's parent nodes outgoing nodes set.
        for parent_node in in_graph[node]:
            out_graph[parent_node].remove(node)
            # Push the parent node into queue if they become nodes with no
            # outgoing edges.
            if not out_graph[parent_node]:
                queue.append(parent_node)
    safe_nodes.sort()
    return safe_nodes

assert eventual_safe_nodes_incoming_and_outgoing_edges([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]

