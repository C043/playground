from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> bool:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return True

            if sum < target:
                left += 1
            else:
                right -= 1

        return False


solution = Solution()
print(solution.twoSum([1, 3, 4, 6, 8, 10, 13], 13))

"""
This is a two pointer pattern problem.

Initialize pointers
Calculate current sum
If current sum is equal to target, return True
If it's smaller than target, move the left pointer
Else move the right pointer
Return False the pointer meet

The time complexity is O(n) linear as we loop over the list just once.
The space complexity is O(1) because we always keep track of a few variables and that's it.
"""
