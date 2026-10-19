from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for index, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[index - k])

        return False


nums = [1, 2, 3, 1]  # True
k = 3
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))
