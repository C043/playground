from typing import List


def dfs(node: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
    colors[node] = color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == 0 and not dfs(neighbor, -color, graph, colors):
            return False
    return True


def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    colors = [0] * len(graph)
    for i in range(len(graph)):
        if colors[i] == 0 and not dfs(i, 1, graph, colors):
            return False
    return True


# True
graph = [[1, 4], [0, 2], [1], [4], [0, 3]]

# True
graph = [[1, 2], [0, 3], [0, 3], [1, 2], [5], [4]]

# False
graph = [[1, 4], [0, 2], [1, 3], [4, 2], [0, 3]]
print(bipartite_graph_validation(graph))

"""
Time complexity is O(n + e) where n denotes the number of nodes and e denotes the number of edges. This is because we explore all nodes in the graph and traverse across e edges during DFS.

Space complexity is O(n) due to the space taken up by the recursive call stack, which can grow as large as n. In addition, the colors array also contributes O(n) space.
"""
