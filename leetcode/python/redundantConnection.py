from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])

            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []


# [1,4]
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

# [2,3]
edges = [[1, 2], [1, 3], [2, 3]]

# [2,8]
edges = [
    [2, 7],
    [7, 8],
    [3, 6],
    [2, 5],
    [6, 8],
    [4, 8],
    [2, 8],
    [1, 8],
    [7, 10],
    [3, 9],
]
solution = Solution()
print(solution.findRedundantConnection(edges))
