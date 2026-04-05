from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [0] * len(graph)

        for i in range(len(graph)):
            if colors[i] == 0 and not self.dfs(i, graph, 1, colors):
                return False
        return True

    def dfs(
        self, node: int, graph: List[List[int]], color: int, colors: List[int]
    ) -> bool:
        colors[node] = color
        for nei in graph[node]:
            if colors[nei] == color:
                return False
            if colors[nei] == 0 and not self.dfs(nei, graph, -color, colors):
                return False
        return True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
graph = [[1], [0, 3], [3], [1, 2]]
solution = Solution()
print(solution.isBipartite(graph))

"""
0 -> 1 -> 3 -> 2
"""
