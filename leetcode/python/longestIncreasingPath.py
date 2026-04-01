from typing import DefaultDict, List


def dfs(
    cell: tuple[int, int],
    matrix: List[List[int]],
    memo: dict[tuple[int, int], int] = DefaultDict(int),
) -> int:
    # We use memoization in order to not calculate the longest paths that we already calculated
    if memo[cell] != 0:
        return memo[cell]

    # For each neighbor we do dfs if the neighbor is bigger than the current cell
    max_path = 1
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dir in dirs:
        next_r, next_c = cell[0] + dir[0], cell[1] + dir[1]

        if (
            next_r < 0
            or next_r >= len(matrix)
            or next_c < 0
            or next_c >= len(matrix[0])
        ):
            continue

        neighbor = matrix[next_r][next_c]

        if neighbor > matrix[cell[0]][cell[1]]:
            max_path = max(max_path, dfs((next_r, next_c), matrix, memo) + 1)
            memo[cell] = max_path

    # We return the max path from the current cell
    # This is a recursive function. This means that it's going to return the max path of every cell in the path from the first cell to the latest one.
    # We use memoization to not calculate the same things twice.
    return max_path


def longest_increasing_path(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0

    max_path = 0
    # We cycle all the cells and for each cell we find the longest path from that cell
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            max_path = max(max_path, dfs((r, c), matrix))

    # In the end we'll have the longest path in the matrix and we return it
    return max_path


matrix = [[1, 5, 8], [3, 4, 4], [7, 9, 2]]
print(longest_increasing_path(matrix))

"""
Time complexity is O(m * n) where m denotes the number of rows, and n denotes the number of columns. This is because each cell of the matrix is visited at most twice: once in the longest_increasing_path function, and during DFS where each cell is visited at most once due to memoization.

Space complexity is O(m * n) primarily due to the recursive call stack during DFS, and the memoization table, both of which can grow to m * n in size.
"""
