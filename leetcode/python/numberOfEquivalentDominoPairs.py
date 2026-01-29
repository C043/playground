from typing import List


class Solution:
    def numEquivDominoPairsBruteForce(self, dominoes: List[List[int]]) -> int:
        result = 0
        for i, domino in enumerate(dominoes):
            for j, secondDomino in enumerate(dominoes[i + 1 :]):
                if (
                    domino[0] == secondDomino[0]
                    and domino[1] == secondDomino[1]
                    or domino[0] == secondDomino[1]
                    and domino[1] == secondDomino[0]
                ):
                    result += 1

        return result

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoMap = dict()
        result = 0
        for domino in dominoes:
            sortedList = sorted(domino)
            key = tuple(sortedList)
            if key in dominoMap:
                dominoMap[key] += 1
                result += 1
            else:
                dominoMap[key] = 1

        return result


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
solution = Solution()
print(solution.numEquivDominoPairs(dominoes))
