from collections import deque
def findMinCost(n, citiesInfo, cLib, cRoad):
	cities = set([i for i in range(1, n+1)])
	graph = {}
	makeGraph(graph, citiesInfo)
	minCost = 0

	while cities:
		q = deque()
		city = cities.pop()
		q.append(city)
		visited = set([city])
		while q:
			node = q.popleft()
			cities.discard(node)
			for neigh in graph[node]:
				if neigh not in visited:
					minCost += cRoad
					q.append(neigh)
					visited.add(neigh)
		minCost += cLib
	return minCost

def makeGraph(graph, info):
	for u, v in info:
		if u not in graph:
			graph[u] = set([v])
		else:
			graph[u].add(v)
		if v not in graph:
			graph[v] = set([u])
		else:
			graph[v].add(u)	
print(findMinCost(7,[[7,1],[1,3],[1,2],[2,3],[5,6],[6,4]], 3, 2))	
