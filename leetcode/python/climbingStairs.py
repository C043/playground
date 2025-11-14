from typing import Dict


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recursiveClimb(memo: Dict[int, int], k: int) -> int:
            if k <= 1:
                return 1

            if k in memo:
                return memo[k]

            result = recursiveClimb(memo, k - 1) + recursiveClimb(memo, k - 2)

            memo[k] = result
            return result

        return recursiveClimb(memo, n)


solution = Solution()
print(solution.climbStairs(44))


"""
This implementation uses memoization in order to store long calculations and optimize time complexity. Without it, we would calculate the same things over and over again, the more the number of stairs, the more times we would calculate the same things over and over again.

In this case we need to know all the possible ways we can climb a n set of stairs using one step or two steps each single stair.
To calculate this we recurively call our helper function that sums the result of possibilities if we take one step plus the same if we take two steps.
It stores the result in the memo dict so if we need it again, we don't have to calculate it again (which possibly means a lot of recursive calls).

The total distinct ways to reach the top using one step or two steps is the sum of the distinct ways to reach the top of n - 1 and n - 2 because (ways(3) = ways(2) + ways(1))
We add them because the group of paths where the last move is a single step and the group of paths where the last move is a double step are completely separate and do not overlap. A path can't end in both a single and double step. To get the total, we have to sum the counts of these separate groups.

Time complexity is O(n) because we use memoization and this ensures that the calculation for any given number of stairs is perfomred exactly once.

Space complexity O(n) because we keep memorized n number of entries in the dict.
"""
