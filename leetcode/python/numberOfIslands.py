from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCounter = 0

        # Walk the grid cell by cell. Each time you hit a '1' that hasn’t been seen before, that means you’ve discovered a new island. Increment your island counter.
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

                # From that starting cell, explore all reachable '1' neighbors (up/down/left/right). You can do this with either a stack/recursion (depth‑first) or a queue (breadth‑first).
                # As you visit cells, mark them so you won’t count them again—either by tracking them in a visited set or by writing over the grid entry.
                # When that exploration finishes, you’ve completely “flooded out” that island. Continue scanning the grid; each untouched '1' you encounter kicks off the same process.

        return islandCounter


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

solution = Solution()
print(solution.numIslands(grid))
