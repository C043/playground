from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recursiveMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(
            self.recursiveMaxDepth(root.left), self.recursiveMaxDepth(root.right)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return 1

        queue: List[TreeNode] = []
        queue.append(root)
        max = 0

        while len(queue) > 0:
            subQueue: List[TreeNode] = queue
            queue = []

            while len(subQueue) > 0:
                node = subQueue.pop()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max += 1

        return max


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, None, TreeNode(2))
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
solution = Solution()
print(solution.recursiveMaxDepth(root))

"""
This implementation uses BFS to calculate the max depth
We create a queue and we push the root inside.
Then we do a nested loop:
We copy the current queue and reset the main one.
While the copy is more than 0:
We pop from the copy and push left and right of the popped node (if they exist) to the main queue.
After the inner loop, we update max because we're sure we processed a level of the tree.
We keep going until we traversed all the tree.
We return the max variable.

The important part in this implementation is how we know that we processed an entire level before adding one to max.
We know thid because at every cycle of the outer while loop, we create a copy of the current main queue. That copy contains all the nodes of the current level. This means that when we process all the copy queue, we know for sure that we processed all the level and populated the next one in the main queue.

The time complexity is O(n) because we process every node only once
The space complexity is O(w) where n is the max width of the tree because we always keep in memory a level at a time
"""
