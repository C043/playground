from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result


height = [4, 2, 0, 3, 2, 5]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [3, 4, 1, 2, 2, 4, 1, 3, 2]
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
print(solution.maxArea(height))

"""
One pass, two pointers, always move the shorter wall.

Initialize pointers
Calculate area
Update max area if necessary
Move pointer on shorter wall
Repeat until pointers are on the same wall

The time complexity is O(n)
The space complexity is O(1)
"""
