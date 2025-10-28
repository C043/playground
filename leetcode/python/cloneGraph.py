class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import List, Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return
        elif not node.neighbors:
            return Node(node.val)

        cloneDict: dict[Node, Node] = {}
        visited = set()
        queue: deque[Node] = deque([node])

        while queue:
            current = queue.popleft()
            cloneDict.setdefault(current, Node(current.val))
            visited.add(current)
            for neighbor in current.neighbors:
                cloneDict.setdefault(neighbor, Node(neighbor.val))
                cloneDict[current].neighbors.append(cloneDict[neighbor])
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return cloneDict[node]


solution = Solution()
root = Node(1, [])
second = Node(2, [])
third = Node(3, [])
forth = Node(4, [])
root.neighbors.append(second)
root.neighbors.append(forth)

second.neighbors.append(root)
second.neighbors.append(third)

third.neighbors.append(second)
third.neighbors.append(forth)

forth.neighbors.append(root)
forth.neighbors.append(third)

solution.cloneGraph(root)

"""
This implementation is O(n) time complexity
This implementation is O(n2) space complexity
"""
