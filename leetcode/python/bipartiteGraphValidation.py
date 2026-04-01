from typing import List


def dfs(node: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
    # Here we set the color of the current node to the color passed to the function. It will be either 1 or -1
    colors[node] = color

    # Then we cycle all the neighbors of the current node
    # If the color of any neighbor is equal to the color of the current node it means that the graph is not bipartite and we return False
    # If not, then we keep going with the dfs passing the opposite of the current node color
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == 0 and not dfs(neighbor, -color, graph, colors):
            return False

    return True


def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    # Here we keep track of all the colors already set. 0 is not set yet. 1 and -1 are the alternating colors
    colors = [0] * len(graph)

    # Here we loop over all the nodes and check if the color is not set for the current node, we start dfs on that node.
    # If the dfs call stack return False it means that the graph is not bipartite and we return False
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
