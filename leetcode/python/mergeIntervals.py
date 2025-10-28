# @leet start


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        solution = []
        currentInterval = intervals[0]

        for interval in intervals[1:]:
            intervalStartingPoint = interval[0]
            intervalEndingPoint = interval[1]

            if (
                intervalStartingPoint <= currentInterval[1]
                and intervalStartingPoint >= currentInterval[0]
            ):
                currentInterval[1] = max(intervalEndingPoint, currentInterval[1])
            else:
                solution.append(currentInterval)
                currentInterval = interval

        solution.append(currentInterval)
        return solution


# @leet end

solution = Solution()
print(solution.merge([[2, 3], [1, 4], [7, 14], [5, 10]]))

"""
This implementation is O(n) space complexity because we save another list that possibly contains the same input elements. 
Even if we loop over the input just once, we sort it in place which is O(n log n)
"""
