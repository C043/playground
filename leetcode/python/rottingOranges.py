from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Put all rotting oranges in a queue
        queue: deque[List[int]] = deque([])
        # Count all oranges that are not rotting
        count = 0
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    count += 1

        # While queue, we add one minute to the minute counter and we traverse the graph putting inside the queue only the oranges
        while queue:
            currentlyRotting = queue
            queue = deque([])
            while currentlyRotting:
                y, x = currentlyRotting.popleft()

                if x + 1 in range(len(grid[y])) and grid[y][x + 1] == 1:
                    grid[y][x + 1] = 2
                    queue.append([y, x + 1])
                    count -= 1
                if x - 1 in range(len(grid[y])) and grid[y][x - 1] == 1:
                    grid[y][x - 1] = 2
                    queue.append([y, x - 1])
                    count -= 1
                if y + 1 in range(len(grid)) and grid[y + 1][x] == 1:
                    grid[y + 1][x] = 2
                    queue.append([y + 1, x])
                    count -= 1
                if y - 1 in range(len(grid)) and grid[y - 1][x] == 1:
                    grid[y - 1][x] = 2
                    queue.append([y - 1, x])
                    count -= 1

            if queue:
                minutes += 1

        # If the count is 0 we return the minutes, if not, we return -1
        return minutes if count == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
solution = Solution()
print(solution.orangesRotting(grid))

"""
This implementation is structured in two steps:
- Loop over the whole grid once to count non rotting oranges and to put the coordinates of the rotting oranges in the queue
- Loop over the queue using BFS graph traversal and with index guards, rotting all the oranges that touch a rotting one. Incrementing the minutes accordingly and reducing the counter of non rotting oranges if this happens.

We return the minutes if the counter of non rotting oranges returns to 0 because it means that it was possible to rot every orange. We return -1 otherwise.

Time complexity is O(m * n) because we loop over every cell in the grid once in the first step and once in the second step in the worst case
Space complexity is O(m * n) because the queue can hold multiple cells at once and in the worst case it could be all the cells in the grid
"""
