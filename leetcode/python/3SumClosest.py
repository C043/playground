from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        currentClosest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            x = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                triplet = x + nums[left] + nums[right]

                if abs(triplet - target) < abs(currentClosest - target):
                    currentClosest = triplet

                if triplet > target:
                    right -= 1
                elif triplet < target:
                    left += 1

        return currentClosest


nums = [0, 0, 0]
solution = Solution()
nums = [0, 1, 2]
print(solution.threeSumClosest(nums, 0))
nums = [-1, 2, 1, -4]
print(solution.threeSumClosest(nums, 1))
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(solution.threeSumClosest(nums, 1))

"""
The time complexity is O(n2)
The space complexity is O(1)
"""
