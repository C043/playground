from collections import defaultdict, deque
from typing import DefaultDict, List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj: dict[int, List[int]] = DefaultDict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edgeCount: dict[int, int] = defaultdict(int)
        leaves: deque[int] = deque()
        for src, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(src)
            edgeCount[src] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                src = leaves.popleft()
                n -= 1

                for neighbors in adj[src]:
                    edgeCount[neighbors] -= 1
                    if edgeCount[neighbors] == 1:
                        leaves.append(neighbors)

        return [0]


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
solution = Solution()
print(solution.findMinHeightTrees(n, edges))


# Build adjecency list
# Count number of edges (for every single nodes, we count the edges)
# We should find the leaves if they have just one edge and we create a leafe queue
# Now we go layer by layer by processing the queue
# For every leaf neighbor, we reduce the edge count of the neighbor because we're trying to find the center of the graph
# We then check if the neighbor has become a leaf
# Every time we pop from the queue, we need to reduce n by one and at the start of the loop we need to check if n is qual or less than 2. Then we return the rest of the queue
# This is because the center of the graph will at max be 2 nodes. It is not possible to have more than 2 nodes as the graph center
# Base case, if we only have one node, we return it

"""
The basic Idea of this implementation is that we need to find the center of the graph and the center can be of one or two nodes.
So, we find the leaves and we traverse the graph from them until we get to the center.
Then we return the center nodes.
That's it.
To do this we create the graph adjacency list
We keep the count of edges that every node has
We find the leaves (that are the nodes that have only one edge)
Then we process every leaf reducing the edges counter of every leaf neighbor and if the neighbor becomes a leaf, we append it to the leaves queue.
Every time we pop a leaf from the queue, we reduce the n variable by one. This is because we're traversing the nodes, but we need to traverse until we arrive at the center (that can be one or two nodes).
When n is <= 2 then it means that the remaining nodes in the queue are the center and we return them.

Time complexity is O(n) as every loop in this method is O(n)
Space complexity is O(n) as we're storing every node in the adj and in the leaves in the worst case
"""
