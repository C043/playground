class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeroes = best = 0

        for right, num in enumerate(nums):
            if num == 0:
                zeroes += 1
                while zeroes > k:
                    if nums[left] == 0:
                        zeroes -= 1
                    left += 1

            best = max(best, (right - left) + 1)

        return best


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
solution = Solution()
print(solution.longestOnes(nums, k))
