from typing import List


def count_islands(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    result = 0

    def dfs(i: int, j: int):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]):
            return

        if matrix[i][j] == 1:
            matrix[i][j] = -1
        else:
            return

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for d in dirs:
            next_r, next_c = i + d[0], j + d[1]
            dfs(next_r, next_c)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            cell = matrix[i][j]
            if cell == 1:
                result += 1
                dfs(i, j)

    return result


# 2
matrix = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
print(count_islands(matrix))

"""
Time complexity is O(m * n), where m denotes the number of rows and n denotes the number of columns. This is because each cell of the matrix is visited at most twice: once when searching for land cells in the count_island function, and up to one more time during DFS.

Space complexity: The space complexity is O(m * n) mostly due to the recursive call stack during DFS, which can gruw up to m * n in size.
"""
