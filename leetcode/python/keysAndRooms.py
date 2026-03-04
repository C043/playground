from collections import deque
from typing import List, Set


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue: deque[int] = deque(rooms[0])
        visited: Set[int] = set()

        while queue:
            key = queue.popleft()

            if key in visited or key == 0:
                continue

            queue.extend(rooms[key])

            visited.add(key)

        return True if len(visited) == len(rooms) - 1 else False


rooms = [[1], [2], [3], []]
solution = Solution()
print(solution.canVisitAllRooms(rooms))

"""
This solution is fairly simple:
- We traverse the graph using BFS graph traversal
- If length of visited is right, we return True, otherwise it means that we did not visit every door

Time complexity is O(n) because we visit every node once
Space complexity is O(n) because visited is going to account for every node once
"""
