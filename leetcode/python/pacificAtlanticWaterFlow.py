from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacificSet = set()
        atlanticSet = set()

        pacificQueue = deque()
        atlanticQueue = deque()

        for r in range(ROWS):
            # Left border
            pacificQueue.append((r, 0))
            pacificSet.add((r, 0))

            # Right border
            atlanticQueue.append((r, COLS - 1))
            atlanticSet.add((r, COLS - 1))

        for c in range(COLS):
            # Top border
            pacificQueue.append((0, c))
            pacificSet.add((0, c))

            # Bottom border
            atlanticSet.add((ROWS - 1, c))
            atlanticQueue.append((ROWS - 1, c))

        def bfs(queue: deque, reachableCellsSet: set):
            while queue:
                currentRow, currentCol = queue.popleft()

                for deltaRow, deltaCol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    neighborRow, neighborCol = (
                        currentRow + deltaRow,
                        currentCol + deltaCol,
                    )

                    if (
                        0 <= neighborRow < ROWS
                        and 0 <= neighborCol < COLS
                        and (neighborRow, neighborCol) not in reachableCellsSet
                        and heights[neighborRow][neighborCol]
                        >= heights[currentRow][currentCol]
                    ):
                        reachableCellsSet.add((neighborRow, neighborCol))
                        queue.append((neighborRow, neighborCol))

        bfs(pacificQueue, pacificSet)
        bfs(atlanticQueue, atlanticSet)

        result = list(pacificSet.intersection(atlanticSet))

        return result


solution = Solution()
print(
    solution.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)

"""
The main concept of this algorithm is that we trace back from the cells touch the oceans creating two separated sets that contains all the cells in the path from the ocean to the rest of the graph.
We do this populating two separated sets and queues with the cells from each border (because those cells surely touch the oceans).
Then we perform the BFS graph traversal adding to the queue and to the set only the neighbors cells that are inside the graph constraints, we did not visit yet and that have their height more or equal to the current cell.
This ensures that the water can drain through those cells because the current cell is lower than the neighbors.

Once we traversed and populated for both oceans, we return the intersection of the two sets because those cells are the complete paths that the water can traverse to reach both oceans. It's kind of smart!

The time complexity is O(R * C) where r are rows and c are columns. We can say that it's O(n) where n is the total number of cells.
This is because we visit every cells at most twice.
Once if the cell can reach the pacific
Once if the cell can reach the atlantic
So if every cell can reach both oceans, we visit every cell twice

The space complexity is O(R * C) or O(n) same as time complexity
This is because we keep two sets that at worst can contain all the cells each (if all the cells can reach both oceans).
Also the queues can become quite large, but they are gradually emptied.
"""
