# https://leetcode.com/problems/find-if-path-exists-in-graph/	
# 2022-11-06 Hongsik Kim

def dfs(start, visited, edges):
	for i in range(len(edges)-1):
		if edges[i][0] == start:
			visited[edges[i][1]] = True
			dfs(edges[i][1], visited, edges)

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    visited = [False]*n
    dfs(source, visited, edges)
    return visited[destination-1]
