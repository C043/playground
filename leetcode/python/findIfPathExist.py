from collections import defaultdict, deque
from typing import Dict, List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjacencyList: Dict[int, List[int]] = defaultdict(list[int])
        visited: Dict[int, bool] = {}

        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])

        queue: deque[int] = deque([source])

        while queue:
            key = queue.popleft()

            if key in visited:
                continue

            if key == destination:
                return True

            neighbors = adjacencyList[key]

            for neighbor in neighbors:
                queue.append(neighbor)

            visited[key] = True

        return False


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

n = 10
edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
source = 7
destination = 5
solution = Solution()
print(solution.validPath(n, edges, source, destination))

"""
This solution creates the adjacency list of the graph and then uses BFS graph traversal starting from the source to find out if there is a path to destination.

Time complexity is O(n + e) because we build the adjacency list and traverse every node once
Space complexity is O(n + e) because we keep track of every adjacency + visited + queue. In the worst case it could be O(n2)
"""
