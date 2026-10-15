class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # We sort the array
        nums.sort()

        n = len(nums)
        # Result array
        result = []

        # We fix two numbers and run the 2sum algorithm to get the other two numbers skipping duplicates every time
        for i in range(n - 3):
            # Skips duplicates on this level
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skips duplicates on this level too
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result


nums = [1, 0, -1, 0, -2, 2]
target = 0
solution = Solution()
print(solution.fourSum(nums, 0))
