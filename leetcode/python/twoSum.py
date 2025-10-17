# @leet start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            for y, b in enumerate(nums[i + 1 :], start=i + 1):
                if a + b == target:
                    return [i, y]


# @leet end


# @leet start
class SolutionOptimized(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in visited:
                return [visited[complement], i]

            visited[num] = i


solution = SolutionOptimized()
print(solution.twoSum([1, 3, 5], 8))

# @leet end
