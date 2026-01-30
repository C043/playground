from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        solution = [0, 0]

        while high > low:
            result = numbers[low] + numbers[high]
            if result == target:
                solution = [low + 1, high + 1]
                break
            elif result > target:
                high -= 1
            elif result < target:
                low += 1

        return solution


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))

"""
This is a two pointer pattern problem.
We start by creating two variables that will be our pointers in the list.
One at the start of the list and one at the end of it.
Then we loop until high is greater than low and we try the sum of the two numbers at those positions:
if it's the target we know the solution and we return it.
If it's greater than the target, we reduce by one the high pointer.
If it's lower than the target, we add one to the low pointer.
This way we can check the whole list with a single loop pass. Otherwise we would need a nested loop but that would be quadratic time while this is linear.

The time complexity is O(n) linear as we loop over the list just once.
The space complexity is O(1) because we always keep track of a few variables and that's it.
"""
