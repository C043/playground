from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]


edges = [[1, 2], [2, 3], [4, 2]]
solution = Solution()
print(solution.findCenter(edges))

"""
This solution is very simple: in a star graph there is only a node that's repeated in every edge. We only need to look at the first two edges to find the common node.

Time complexity is O(1)
Space complexity is O(1)
"""
