from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisitesCount: dict[int, int] = {}
        courseDependencies: dict[int, List[int]] = {}
        return true


solution = Solution()
print(solution.canFinish(2, [[1, 0], [0, 1]]))
