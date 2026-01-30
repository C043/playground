from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
                right -= 1

        return water


height = [4, 2, 0, 3, 2, 5]
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
solution = Solution()
print(solution.trap(height))

"""
This implementation is based on the fact that: water is trapped by the shorter of the tallest walls on both sides.

We create two pointers, one at the start of the array, and one at the end of the array.
We create empty variables to keep track of the tallest wall from the left and from the right
And of course we create a varable to store the trapped water.

Then we loop while left is less than right.
We check if the left is smaller than the right.
If so, we update left max wall, water and we go up by one in left.
We calculate water summing up the left max wall minus the left height (the current one).
If not, we do the same from the right with the only difference that we reduce right by one.

Then we return the water.

The time complexity is O(n)
The space complexity is O(1)
"""
