from collections import deque
from typing import List


def matrix_infection(matrix: List[List[int]]) -> int:
    dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    queue: deque[tuple[int, int]] = deque()
    ones = 0
    seconds = 0

    # We find all 2s and all 1s
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            cell = matrix[r][c]
            if cell == 2:
                queue.append((r, c))
            elif cell == 1:
                ones += 1

    # We do multi BFS
    while queue and ones > 0:
        seconds += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dir in dirs:
                next_r, next_c = r + dir[0], c + dir[1]

                if (
                    next_r < 0
                    or next_r >= len(matrix)
                    or next_c < 0
                    or next_c >= len(matrix[0])
                ):
                    continue

                cell = matrix[next_r][next_c]
                if cell == 1:
                    matrix[next_r][next_c] = 2
                    ones -= 1
                    queue.append((next_r, next_c))

    # We return the result if possible, otherwise we return -1
    return seconds if ones == 0 else -1


matrix = [[1, 2, 1, 0, 1], [1, 0, 0, 1, 1], [1, 2, 0, 0, 2]]
matrix = [[2, 2, 2], [0, 0, 0], [1, 0, 0]]
print(matrix_infection(matrix))

"""
Time complexity is O(m * n) where m denotes the number or rows, and n denotes the number of columns.
This is because in the worst case, every cell in the matrix is explored during level-order traversal.

Space complexity is O(m * n), primarily due to the queue, which can store up to m * n cells
"""
