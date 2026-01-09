from typing import List

# @leet start


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        bestTwoBack: int = 0
        bestOneBack: int = 0

        for num in nums:
            takeThis = bestTwoBack + num
            skipThis = bestOneBack

            bestHere = max(takeThis, skipThis)
            bestTwoBack = bestOneBack
            bestOneBack = bestHere

        return bestOneBack


solution = Solution()
print(solution.rob([1, 2, 3, 1]))
print(solution.rob([2, 7, 9, 3, 1]))

# @leet end

"""
Explanation:
This implementation is based on the fact that you can't rob two houses next to each other and you need to find the max amount of money you can rob without getting caught.

We keep two variables in memory:
The best money we can make two houses ago and the best money we can make one house ago.
In the loop is where the magic happens:
We build two variables based on the best two and one house back
takeThis is if we rob this house, so we can only add the best from two houses back.
skipThis is if we skip this house, so we just take the best up until the previous house.
These two variables are the two options for this house.
bestHere is the max from the two variables. Here is where we decide the maximum money we can make from the beginning up until this house.
We then update the two variables and we keep going with the loop.
When the loop is finished we return the bestOneBack because at this point it holds the best total up to the last house.

This implementation is O(n) because we loop the nums just once and at the end of the loop we have the solution so the time it takes to finish the algorithm is fixed and grows linearly with the len(nums).

This implementation is O(1) space complexity because we only keep in memory a fixed amount of variables.
"""
