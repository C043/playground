from collections import defaultdict, deque
from typing import DefaultDict, Dict, List


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
            print(key)
            print(neighbors)

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
