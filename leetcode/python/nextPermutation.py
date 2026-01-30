from typing import List
import math


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        elif len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        # We find the pivot
        pivot = -1
        left = len(nums) - 2
        right = len(nums) - 1
        while left >= 0:
            if nums[left] < nums[right]:
                pivot = left
                break

            left -= 1
            right -= 1

        # We handle the last permutation
        if pivot == -1:
            nums.reverse()
            print(nums)
            return

        # We find the smallest greatest than pivot
        smallestGreaterThanPivot = pivot + 1
        for i in range(pivot + 2, len(nums)):
            if nums[i] > nums[pivot]:
                smallestGreaterThanPivot = (
                    i
                    if min(nums[smallestGreaterThanPivot], nums[i]) == nums[i]
                    else smallestGreaterThanPivot
                )

        # We swap the pivot and the smallest greatest than pivot
        nums[pivot], nums[smallestGreaterThanPivot] = (
            nums[smallestGreaterThanPivot],
            nums[pivot],
        )

        # We reverse the suffix
        left = pivot + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


nums = [3, 2, 1]
nums = [1, 2, 3]
nums = [1, 3, 2]
solution = Solution()
solution.nextPermutation(nums)
