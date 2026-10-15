class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0

        for k in range(len(nums) - 1, 1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


nums = [2, 2, 3, 4]
solution = Solution()
print(solution.triangleNumber(nums))
