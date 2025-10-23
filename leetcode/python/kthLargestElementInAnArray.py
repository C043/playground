import heapq
import random
from typing import List


# Using just a min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heapq.heappop(heap)


class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p < k:
                return quickselect(p + 1, r)
            if p > k:
                return quickselect(l, p - 1)
            else:
                return nums[p]

        return quickselect(0, len(nums) - 1)


solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))

"""
These are two implementations.
One uses a heap to always keep in memory the k max values in the array and return the first value of the heap.
The time complexity of this implementation is O(n log k) because it uses a heap of length k. (Operations like push and pop on the heap are O(log k)).
The space complexity of this implementation is O(k) because we keep a heap in memory of length k.

The other implementation uses quick select.
Quick select reduces the time complexity to O(n) in average cases.
The only problem is with arrays with many duplicates. With many duplicates every round we shrink the search window by only one slot (the pivot itself), so you still scan almost the entire array at each level. That turns the supposed linear average into quadratic time.
The space complexity is O(1) because we just keep some variables saved through all the algorithm.

Quick select theory:
- Pick a random "pivot" and move it aside
- Walk through the array of numbers once, putting every smaller number than the pivot on its left and everything bigger on its right (you're just splitting around the pivot)
- Now the pivot sits exactly where it would be in sorted order. Count how many numbers ended up on its left - that's its rank.
- If that rank matches the one you want, you're done because the pivot is your number. (Even if we're looking for the kth largest, it's easier to just count from the left because biggest is the same as n - k)
- If you still need a smaller rank, ignore the left numbers and repeat with the right pile (adjusting k because you threw some cards away)
Because each round throws away a big chunk of the numbers, you usually fin your card after looking at just a couple of smaller piles instead of sorting everything.
"""
