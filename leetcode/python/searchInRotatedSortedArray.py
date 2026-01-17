from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            # If the left half is sorted
            if nums[low] <= nums[mid]:
                # We check if target is in this half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # If the left half is not sorted
            else:
                # We check if the target is in the right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print("v4")
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print("v-1")
print(solution.search([5, 6, 0, 1, 2, 3, 4], 3))
print("v5")
print(solution.search([4, 5, 6, 0, 1, 2], 5))
print("v1")
print(solution.search([1], 0))
print("v-1")
print(solution.search([1, 0], 0))
print("v1")
print(solution.search([5, 1, 2], 5))
print("v0")

"""
This implementation uses a modified binary search.
At each iteration, we check whether the left half of the array is sorted or not.
If it's sorted, we check if the target is in that half, if it's not sorted, we check if the target is in the right half (as we're sure that the right half is sorted).
We keep going until we find the target.

The space complexity of this algorithm is O(1) as we only keep in memory a few pointers

The time complexity of this algorithm is O(log n) because the loop runs log2(n) times like binary search.
"""
