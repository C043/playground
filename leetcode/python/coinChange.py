from collections import defaultdict
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = defaultdict(lambda: INF)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        ans = dp[amount] if dp[amount] != INF else -1

        return ans


solution = Solution()
print(solution.coinChange([1, 2, 5], 11))

"""
This implementation uses the Bottom-up DP constructions and minimal combination logic to solve the problem.
The main logic behind it is that we create a map of already solved solutions starting with the 0 that will always be 0 and stating the default amount + 1 for all the others.
Then we solve each number from 1 to amount with a nested loop.
For each number in range(1, amount), we try each coin in coins.
if coin is less than or equal to the number we're currently checking, we just add to the map for the key = number we're currently checking, the minimum between the already saved value in the map for the current number and the already saved value in the map for the (current number - coin) + 1.
If we already solved the current number, we're just going to leave it as that. If we didn't, we add 1 to the already solved i - coin solution.

After the loops, we have all the solutions from 0 to amount in the map, so we'll just need to return the map[amount] one if it's not INF, otherwise we return -1 stating that the problem is not solvable with the list of coins.

The time complexity is O(c * a) where c is the len(coins) and a is the amount.
This is because we have a nested loop that depends on those lens.

The space complexity is O(a) because of the map where a is the amount.
This is because the map grows linearly as the amount grows.
"""
