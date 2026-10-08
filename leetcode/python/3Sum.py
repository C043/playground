from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                # We already checked this number
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))

"""
Sort the array
Fix one element
Use the two pointer technique to find matching pairs
Handle duplicates at both levels

Since it's a nested loop, the time complexity is O(n2).
For the space complexity it's O(1) as we don't store anything but some variables.
"""
