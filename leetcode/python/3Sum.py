from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            x = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = x + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
print(solution.threeSum(nums))

"""
Here we sort the nums and then through a nested loop we fix one number and we use a two pointer algorightm to test it with the smallest numbers and with the highest numbers in the list after the fixed one.
We adjust the pointers accordingly.
When we find that the sum is 0, we found a triplet, we reduce the list by adding one to left and subtracting one to right. This way we keep trying to find other triplets.
When we find a triplet, we prune all the adjacent duplicates because we cannot use the same triplets.
We do this O(n) times.

Since it's a nested loop, the time complexity is O(n2).
For the space complexity it's O(1) as we don't store anything but some variables.
"""
