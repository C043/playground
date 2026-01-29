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
        counts = dict()
        for a, b in dominoes:
            key = (a, b) if a >= b else (b, a)
            counts[key] = counts.get(key, 0) + 1

        return sum(c * (c - 1) // 2 for c in counts.values())


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6]]
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
solution = Solution()
print(solution.numEquivDominoPairs(dominoes))

"""
The main idea behind this implementation is that we count how many times every domino is present in the input conforming its key so that every compatible domino is saved with the same key.
Then we sum the pairs and we return them.

The time complexity of the optimized solution is O(n) where n is the number of dominoes in the input
The space complexity of the same solution is O(n) in the worst case because we store each domino as a key in a map (we save its count in the map, but in the worst case that means we'll have a key value for each domino in the input)
"""
