from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCounter = 0

        visited = set()
        queue = deque()
        for y, line in enumerate(grid):
            yBoundary = len(grid)
            for x, cell in enumerate(line):
                xBoundary = len(line)
                if (x, y) in visited:
                    continue

                if cell == "1":
                    islandCounter += 1
                    queue.append((cell, x, y))
                    visited.add((x, y))
                    while queue:
                        cell, cx, cy = queue.popleft()

                        if cx + 1 < xBoundary:
                            right = (grid[cy][cx + 1], cx + 1, cy)
                            if right[0] == "1" and (right[1], right[2]) not in visited:
                                queue.append(right)
                                visited.add((right[1], right[2]))
                        if cx - 1 >= 0:
                            left = (grid[cy][cx - 1], cx - 1, cy)
                            if left[0] == "1" and (left[1], left[2]) not in visited:
                                queue.append(left)
                                visited.add((left[1], left[2]))
                        if cy + 1 < yBoundary:
                            down = (grid[cy + 1][cx], cx, cy + 1)
                            if down[0] == "1" and (down[1], down[2]) not in visited:
                                queue.append(down)
                                visited.add((down[1], down[2]))
                        if cy - 1 >= 0:
                            up = (grid[cy - 1][cx], cx, cy - 1)
                            if up[0] == "1" and (up[1], up[2]) not in visited:
                                queue.append(up)
                                visited.add((up[1], up[2]))

                visited.add((x, y))

        return islandCounter

    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        islandCounter = 0

        visited = set()
        stack = []
        for y, line in enumerate(grid):
            yBoundary = len(grid)
            for x, cell in enumerate(line):
                xBoundary = len(line)
                if (x, y) in visited:
                    continue

                if cell == "1":
                    islandCounter += 1
                    stack.append((cell, x, y))
                    visited.add((x, y))
                    while stack:
                        cell, cx, cy = stack.pop()

                        if cx + 1 < xBoundary:
                            right = (grid[cy][cx + 1], cx + 1, cy)
                            if right[0] == "1" and (right[1], right[2]) not in visited:
                                stack.append(right)
                                visited.add((right[1], right[2]))
                        if cx - 1 >= 0:
                            left = (grid[cy][cx - 1], cx - 1, cy)
                            if left[0] == "1" and (left[1], left[2]) not in visited:
                                stack.append(left)
                                visited.add((left[1], left[2]))
                        if cy + 1 < yBoundary:
                            down = (grid[cy + 1][cx], cx, cy + 1)
                            if down[0] == "1" and (down[1], down[2]) not in visited:
                                stack.append(down)
                                visited.add((down[1], down[2]))
                        if cy - 1 >= 0:
                            up = (grid[cy - 1][cx], cx, cy - 1)
                            if up[0] == "1" and (up[1], up[2]) not in visited:
                                stack.append(up)
                                visited.add((up[1], up[2]))

                visited.add((x, y))

        return islandCounter


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

solution = Solution()
print(solution.numIslandsDFS(grid))

"""
In this implementation of graph traversal, we create a counter to return in the end representing the number of islands in the grid.
We initialize a visited set to mark the visited cells in the grid.
We initialize a queue.
We loop over each cell using a nested loop and set the boundaries of the grid.
If we visited the cell, we skip.
At the first 1 cell that we encounter, we add one to the counter and start checking all its neighbors and its neighbors' neighbors until we find all the 1s.
After that we keep iterating until we find another 1 not visited. That means we found another island!
When we iterated all the cells, we return the counter.

In the first DFS implementation, we just replace the queue with a stack to change the order in which we explore the islands.
"""
