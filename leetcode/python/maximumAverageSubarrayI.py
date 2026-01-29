from typing import List
import math


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        windowSum = sum(nums[:k])
        maxSum = windowSum

        for i in range(k, len(nums)):
            windowSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, windowSum)

        return maxSum / k


nums = [0, 1, 1, 3, 3]
nums = [
    8860,
    -853,
    6534,
    4477,
    -4589,
    8646,
    -6155,
    -5577,
    -1656,
    -5779,
    -2619,
    -8604,
    -1358,
    -8009,
    4983,
    7063,
    3104,
    -1560,
    4080,
    2763,
    5616,
    -2375,
    2848,
    1394,
    -7173,
    -5225,
    -8244,
    -809,
    8025,
    -4072,
    -4391,
    -9579,
    1407,
    6700,
    2421,
    -6685,
    5481,
    -1732,
    -8892,
    -6645,
    3077,
    3287,
    -4149,
    8701,
    -4393,
    -9070,
    -1777,
    2237,
    -3253,
    -506,
    -4931,
    -7366,
    -8132,
    5406,
    -6300,
    -275,
    -1908,
    67,
    3569,
    1433,
    -7262,
    -437,
    8303,
    4498,
    -379,
    3054,
    -6285,
    4203,
    6908,
    4433,
    3077,
    2288,
    9733,
    -8067,
    3007,
    9725,
    9669,
    1362,
    -2561,
    -4225,
    5442,
    -9006,
    -429,
    160,
    -9234,
    -4444,
    3586,
    -5711,
    -9506,
    -79,
    -4418,
    -4348,
    -5891,
]
solution = Solution()
print(solution.findMaxAverage(nums, 93))

"""
The base idea behind this implementation is simple.
Since the subarray length is constant, the bigger the sum, the bigger the average.
This means that we don't have to calculate the average every time, we just need to get the maximum subarray sum and return that divided by k to get the average.
We keep track of the window sum and we keep track of the maximum sum
We start the window sum by summing the first window, from index 0 to index k - 1.
This is also our max sum right now.

Then we start a loop from k until the list is over.
We subtract the number just before the window and we sum the new number in the window to the window sum as the window is moving.
We update the max sum if the window sum is higher than the current max sum.
At the end of the loop, we'll have the max sum that we can divide by k and return it to get the maximum average.

This implementation is O(n) in time complexity as it grows linearly with the nums list length.

The space complexity is O(1) because we just keep track of some variables.
"""
