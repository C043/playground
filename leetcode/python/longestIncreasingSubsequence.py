from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []
        for num in nums:
            i = bisect_left(tail, num)
            if i == len(tail):
                tail.append(num)
            else:
                tail[i] = num

        return len(tail)


solution = Solution()
print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

"""
This implementation uses a tail array and a binary search optimization in order to keep an ordered increasing sequence. We need tail to be able to know the length of the longest increasing subsequence. It's not the subsequence itself.
We loop over the nums and we use bisect_left to get the index of the element in tail to replace with the current num. If there aren't any, it means that the current num is bigger than any of the nums in tail so we add it to the list increasing it.

We return len(tail) which is exactly what tail represent.

The time complexity of this implementation is O(n log n) because we loop over every number which is O(n) but for every number we do a binary search using bisect_left. That's log n. So O(n * log n) is the time complexity.

The space complexity is O(n) because we could store the entire nums list in the tail in the worst case.
"""
