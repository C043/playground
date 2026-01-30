from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0

        return 0


height = [4, 2, 0, 3, 2, 5]
solution = Solution()
print(solution.trap(height))
