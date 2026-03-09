from typing import List, Set


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited: Set[int] = set()
        result = 0

        def check(i, j):
            node = isConnected[i][j]
            if node == 0:
                return
            elif int(f"{i}{j}") in visited:
                return

            # We put the nodes in visited so we don't visit them more than once
            visited.add(int(f"{i}{j}"))

            if j + 1 in range(len(isConnected[i])):
                check(i, j + 1)
            if j - 1 in range(len(isConnected[i])):
                check(i, j - 1)
            if i + 1 in range(len(isConnected)):
                check(i + 1, j)
            if i - 1 in range(len(isConnected)):
                check(i - 1, j)

        # Loop over the graph
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if int(f"{i}{j}") in visited:
                    continue

                city = isConnected[i][j]
                # When we visit a 1 node, we explore all its surroundings recursively until we sto finding 1s
                # We up the counter by one because we found a provence
                if city == 1:
                    result += 1
                    check(i, j)

        return result


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution = Solution()
print(solution.findCircleNum(isConnected))
