class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1]
                    )

        return int(cache[0][0])


solution = Solution()
print(solution.minDistance("horse", "ros"))

"""
This implementation uses a 2D DP grid where in each cell we have the minimum edit actions we need to make in order to match the suffix word1[i:] into word2[j:].

  +---+---+---+---+---+
  |   | r | o | s | _ |
  +---+---+---+---+---+
  | h | 3 | 3 | 4 | 5 |
  +---+---+---+---+---+
  | o | 3 | 2 | 3 | 4 |
  +---+---+---+---+---+
  | r | 2 | 2 | 2 | 3 |
  +---+---+---+---+---+
  | s | 3 | 2 | 1 | 2 |
  +---+---+---+---+---+
  | e | 3 | 2 | 1 | 1 |
  +---+---+---+---+---+
  | _ | 3 | 2 | 1 | 0 |
  +---+---+---+---+---+

We add a column and a row because we need the base case as this implementation is a bottom-up dp resolution.
We start from the base case we already know in order to populate the whole table.
Once we populated the base cases, we do a nested loop where we check each word letter starting from the latest letter.
If they are the same, we don't need to do any operation, so we populate that cell in the grid with the grid[i + 1][j + 1] which is the minimum operations we needed from the previous suffix.
It they are not the same, then we add one to the minimum operation needed if we added one character, removed one character, or replaced one character: grid[i + 1][j], grid[i][j + 1], grid[i + 1][j + 1]
Once the nested loop finished, we populated the entire grid.
We just return the first cell, the solution to the whole problem.

The time complexity is O(n * m) where n is len(word1) and m is len(word2), this is because it's directly dependant by the length of both words since there is a nested loop each dependant on the length of one word.

The space complexity is O(n * m) too because we keep in memory the whole 2D grid that's based on both words.
"""
