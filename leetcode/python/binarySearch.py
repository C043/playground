from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


solution = Solution()
print(solution.search([1, 2, 3, 4, 5], 1))
print(solution.search([1, 2, 3, 4, 5], 5))
print(solution.search([1, 2, 3, 4, 5], 6))

"""
This implementation works by dividing the array by half every time.
It works because we know that the numbers are ordered in the array so we check the mid element.
If the mid element is lower than the target, we shrink the array to eliminate the half that's too low.
Then we do it again, and if the element is higher, we shrink again to eliminate the half that's too high.
This until we find the right element.
Or not find it. In that case we return -1.

The space complexity of this algorithm is O(1) because we keep in memory only a couple of variables.
The time complexity of this algorithm is O(log n) because the loop runs about log2(n) times because we eliminate half array each step.
"""
