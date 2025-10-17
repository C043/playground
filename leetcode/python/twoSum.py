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

"""
In this leetcode we see two ways of implementing the solution, one is optimized and the other is not.
The first one uses two nested loops that brute force the solution. This is O(n+^2) because of the two loops. We have to loop over the array two times (in the worst case scenario)
Here the space complexity is optimal though because we don't store anything besides the loops: O(1)

The second one uses an hashmap to store the visited numbers with their indeces and a single loop. Since we have a target, we can get the exact number we need to complete it using the current number in the single loop. If we visited the number already, we'll have it in the map, if not, we add the current number to the map.
This implementation is O(n) because we loop through the array one time only.
Space complexiti is O(n) too because we store all the array in the worst case scenario.

This means that if we have a limited memory system, the brute force optimization could still be the best one.
"""
