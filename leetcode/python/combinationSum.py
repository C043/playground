from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = []

        def backtrack(
            startingIndex: int,
            remainingTarget: int,
            path: List[int],
        ):
            if remainingTarget == 0:
                result.append(path.copy())

            for startingIndex in range(startingIndex, len(candidates)):
                if candidates[startingIndex] > remainingTarget:
                    break
                path.append(candidates[startingIndex])
                backtrack(
                    startingIndex, remainingTarget - candidates[startingIndex], path
                )
                path.pop()

        backtrack(0, target, [])
        return result


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))

"""
This implementation uses a backtrack recursive algorithm.
The helper recursive function takes three arguments: the starting index to check in the candidates array, the remaining target and the path.
We need the starting index because we can reuse candidates but we cannot go backwards in checking candidates. Once we checked a candidate enough, we can only go forward. 
We need the remaining target as we're going to pass the remaining target - the current candidate to the backtrack algorithm.
The path is the current list of candidates we're checking to see if they work. If they work, we'll append a copy of the path to the result list.
So first of all we sort the candidates list. This helps a lot because it permits us to not check all candidates that are bigger than the target.
Then we initiate an empty result list that we're going to return in the end.
Then we define the backtrack recursive function with base case remaining target == 0 (this means that the current path is a possible result and we add a copy of it to the result list).
Then we start a loop from the starting index that is going to be 0 the first time until we loop over all the candidates list.
If the candidate is bigger than the remaining target, we break out of the loop because we can stop looking, from there on, the candidates are all too big.
We append the candidate to the current path and we call the backtrack function again with the current index and the remaining target minus the current candidate and the current path. We do this because we used the first candidate, then we pop from the path.
We pop to restore the shared path to the exact state it had before the recursive call so the next candidate can be tried cleanly.

We append to choose a candidate
We recurse to explore all combinations that start with that choice
We pop to undo that choice so the next iteration starts from the prior state

The time complexity is exponential O(n^(T/s)) with s = smallest candidate n = number of candidates and T = target value
The space complexity is O(T/s) (recursion dept + path), plus output size
"""
