from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Dimensions of the grid
        number_of_rows = len(matrix)
        number_of_columns = len(matrix[0])

        # Queue used for BFS
        # It will initially contain the coordinates of ALL the zeros
        bfs_queue = deque()

        # A value that represents "infinite distance"
        # The maximum possible distance in the grid cannot exceed rows * cols
        INFINITE_DISTANCE = number_of_rows * number_of_columns

        # ---------------------------------------------------------
        # STEP 1: Initialization
        #
        # We prepare the grid for BFS:
        # - All zero cells are starting points (distance = 0)
        # - All one cells are set to "infinite distance"
        #
        # All zeros are also inserted into the BFS queue.
        # This is why this algorithm is called "multi-source BFS":
        # the BFS starts simultaneously from multiple nodes.
        # ---------------------------------------------------------
        for row_index in range(number_of_rows):
            for column_index in range(number_of_columns):

                if matrix[row_index][column_index] == 0:
                    # This cell is a source of distance
                    bfs_queue.append((row_index, column_index))

                else:
                    # This cell is a 1, we don't yet know the distance
                    matrix[row_index][column_index] = INFINITE_DISTANCE

        # ---------------------------------------------------------
        # Directions used to explore the 4 adjacent cells
        #
        # down, up, right, left
        # ---------------------------------------------------------
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # ---------------------------------------------------------
        # STEP 2: Multi-source BFS
        #
        # The BFS expands like a wave starting from all zeros.
        # Each step increases the distance by 1.
        #
        # Because BFS explores level-by-level, the FIRST time we
        # reach a cell we are guaranteed to have found the shortest
        # distance to a zero.
        # ---------------------------------------------------------
        while bfs_queue:

            current_row, current_column = bfs_queue.popleft()

            # Explore all 4 neighbours
            for row_offset, column_offset in directions:

                neighbour_row = current_row + row_offset
                neighbour_column = current_column + column_offset

                # Check that the neighbour is inside the grid
                if (
                    0 <= neighbour_row < number_of_rows
                    and 0 <= neighbour_column < number_of_columns
                ):

                    # If the neighbour still has infinite distance,
                    # it means we have not visited it yet.
                    if matrix[neighbour_row][neighbour_column] == INFINITE_DISTANCE:

                        # Update the neighbour's distance
                        matrix[neighbour_row][neighbour_column] = (
                            matrix[current_row][current_column] + 1
                        )

                        # Add the neighbour to the BFS queue so it can expand further
                        bfs_queue.append((neighbour_row, neighbour_column))

        # The matrix now contains the shortest distance to the nearest zero
        return matrix


mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
solution = Solution()
print(solution.updateMatrix(mat))
