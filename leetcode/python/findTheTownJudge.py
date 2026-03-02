from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        adjacencyList: dict[int, list] = DefaultDict(list)
        suspects: dict[int, bool] = defaultdict(lambda: True)

        for i in range(len(trust)):
            edge = trust[i]
            suspects[edge[0]] = False
            adjacencyList[edge[1]].append(edge[0])

        for i in range(1 + n):
            suspect = adjacencyList[i]
            if suspects[i] and len(suspect) == n - 1:
                return i

        return -1


trust = [[1, 2]]
trust = [[1, 3], [2, 3]]
trust = [[1, 3], [2, 3], [3, 1]]
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
solution = Solution()
print(solution.findJudge(4, trust))

"""
This solution uses two dicts:
- One is the adjacency list that we populate with the trust (each key include all the other people that trust it)
- The other one keeps track of the potential suspects (every time we look through the trust list, we set the current people trusting as false in this one because the judge trusts no one)

When we populated these two dicts, we proceed to loop over n in order to find the judge:
- If the people that trust the current suspect is equal to n - 1 (so not counting himself) and is True in the suspect list, then we return him

If no one satisfy these two conditions, then we return -1 as there is no judge

Time complexity is O(n) as we loop over every person from 1 to n
Space complexity is O(n) as we store each relationship in the dict
"""
