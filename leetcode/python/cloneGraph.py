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
This implementation is O(n + e) time complexity where n are the nodes and e are the edges. In the worst case it's O(n2) because the two numbers could be equal
This is because we loop over every node, but for each node we loop over every neighbor too.

This implementation is O(n + e) space complexity because we save each node in the visited set and queue, but we keep saving the neighbors in the clone nodes too. This too can be O(n2) in the worst case because the nodes and edges could be equal.

We initialize a map where the key are the original nodes and the values are the clones
We initialize a visited set where we'll put all the nodes we visit
We Initialize a queue with the root of the graph inside

We loop until the queue is empty
We pop from the queue
We add the node we just popped to the visited set and we create a default entry in the map
For each of its neighbors, we create a default entry in the map and we append it to the neighbors of the clone of the current node
If the neighbor is not in visited, we add it to the queue and to the visited. This way we're not revisiting nodes
We return the root clone
"""
