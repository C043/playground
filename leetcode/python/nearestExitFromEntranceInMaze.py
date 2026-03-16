from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        queue: deque[tuple[int, int, int]] = deque([(entrance[0], entrance[1], 0)])
        visited: set[tuple[int, int]] = {(entrance[0], entrance[1])}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, steps = queue.popleft()

            # if it's on the border and it's not the entrance, it's an exit
            if (r, c) != (entrance[0], entrance[1]) and (
                r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            ):
                return steps

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and maze[nr][nc] == "."
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1


maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]

maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

maze = [[".", "+"]]
entrance = [0, 0]

maze = [
    [".", "+", "+", "+", ".", ".", ".", "+", "+"],
    [".", ".", "+", ".", "+", ".", "+", "+", "."],
    [".", ".", "+", ".", ".", ".", ".", ".", "."],
    [".", "+", ".", ".", "+", "+", ".", "+", "."],
    [".", ".", ".", ".", ".", ".", ".", "+", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "+", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "+"],
    ["+", ".", ".", ".", "+", ".", ".", ".", "."],
]
entrance = [5, 6]
solution = Solution()
print(solution.nearestExit(maze, entrance))

"""
This solution uses BFS to traverse the graph.
When we reach an exit, we return the steps because in BFS we visit the cells in distance levels from the start.
If we do not encounter any exit, we return -1.

Time complexity is O(mn) because in the worst case scenario we visit every cell once
Space complexity is O(mn) because in the worst case scenario we store every at the same time in queue and visited
"""
