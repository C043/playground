from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        target = len(graph) - 1
        stack = [(0, [0])]

        while stack:
            node, path = stack.pop()

            if node == target:
                result.append(path)
                continue

            for nei in graph[node]:
                stack.append((nei, path + [nei]))

        return result


graph = [[1, 2], [3], [3], []]
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
solution = Solution()
print(solution.allPathsSourceTarget(graph))
