from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1

        print(nums)


nums = [2, 0, 4, 0, 9]
solution = Solution()
print(solution.moveZeroes(nums))
