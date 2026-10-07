from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        currentMax = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            currentArea = width * height

            currentMax = max(currentMax, currentArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return currentMax


height = [4, 2, 0, 3, 2, 5]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [3, 4, 1, 2, 2, 4, 1, 3, 2]
solution = Solution()
print(solution.trap(height))

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
