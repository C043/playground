# @leet start
from typing import List


class Solution(object):
    def merge(self, intervals: List[List[int]]):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort the intervals by their starting point (decide if in place or returning a new list)
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        solution = []
        currentInterval: List[int] = sortedIntervals[0]

        for interval in sortedIntervals[1:]:
            intervalStartingPoint = interval[0]
            intervalEndingPoint = interval[1]

            if (
                intervalStartingPoint <= currentInterval[1]
                and intervalStartingPoint >= currentInterval[0]
            ):
                # merge
                currentInterval[1] = max(intervalEndingPoint, currentInterval[1])
            else:
                solution.append(currentInterval)
                currentInterval = interval

        solution.append(currentInterval)
        return solution


# @leet end

solution = Solution()
print(solution.merge([[2, 3], [1, 4], [7, 14], [5, 10]]))
