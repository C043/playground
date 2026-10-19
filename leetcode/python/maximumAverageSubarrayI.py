class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum

        for i in range(k, len(nums)):
            currentSum = currentSum + nums[i] - nums[i - k]
            maxSum = max(maxSum, currentSum)

        return maxSum / k


nums = [1, 12, -5, -6, 50, 3]  # 12.75000
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))
