from typing import List


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1

        return []


solution = Solution()
nums = [2, 7, 11, 15]
target = 9

solution.twoSum(nums, target)
