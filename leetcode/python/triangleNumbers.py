from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count: int = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1

            while left < right:
                sum = nums[left] + nums[right]
                if sum > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


nums = [11, 4, 9, 6, 15, 18]
solution = Solution()
print(solution.triangleNumber(nums))

"""
Sort the array
Fix the largest number
Two pointer to find pairs that match the condition checking only if their sum is greater than the fixed largest number
If so, we have found right - left triplets, we move right
If not, the pair needs to be bigger, we move left

Time complexity: O(n2)
Space complexity: O(1)
"""
