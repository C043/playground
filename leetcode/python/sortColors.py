from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            currentNum = nums[mid]
            if currentNum == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif currentNum == 1:
                mid += 1
            elif currentNum == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


solution = Solution()
solution.sortColors([2, 0, 2, 1, 1, 0])

"""
This is the Dutch flag partition and it's extremely useful to sort a list in place where there are three macro groups.
It uses three pointers in order to swap values efficiently in the three groups.

The time complexity is O(n) because we loop over all the list just once.
The space complexity is O(1) becuase we just swap values over in place.

This is extremely efficient.
"""
