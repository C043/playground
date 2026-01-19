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
                return result

            for startingIndex in range(startingIndex, len(candidates)):
                if candidates[startingIndex] > remainingTarget:
                    break
                path.append(candidates[startingIndex])
                backtrack(
                    startingIndex, remainingTarget - candidates[startingIndex], path
                )
                path.pop()

            return result

        return backtrack(0, target, [])


solution = Solution()
print(solution.combinationSum([2, 3, 6, 7], 7))

"""

"""
