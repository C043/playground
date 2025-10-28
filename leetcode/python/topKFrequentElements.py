from collections import defaultdict
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        minHeap = []

        for num in nums:
            freqMap[num] += 1

        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return [num for _, num in minHeap]


solution = Solution()
# print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(solution.topKFrequent([5, 3, 1, 1, 1, 3, 73, 1], 2))

"""
Here we implement a min heap in order to always have the right amount of values to return based on k
This implementation is O(n log k) time complexity where n is the len(nums) and k is the number of top frequency elements to return because we maintain a min heap of k length. This means that each time we push or pop, from the heap, we do a O(log k) operation. If we only have unique numbers, we save do this n times.

This implementation is O(n) space complexity because we keep track of all the frequencies. Also the heap is we keep saved is of k lenght, but since k is <= n, for simplicity we say O(n).
"""
