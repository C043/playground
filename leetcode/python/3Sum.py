from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        i = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum > 0:
                    right -= 1
                else:
                    left += 1

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
