from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack: List[tuple[TreeNode, int]] = [(root, root.val)]
        count = 0

        while stack:
            node, maxSoFar = stack.pop()

            if node.val >= maxSoFar:
                count += 1
                maxSoFar = node.val

            if node.right:
                stack.append((node.right, maxSoFar))
            if node.left:
                stack.append((node.left, maxSoFar))

        return count


root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(1), TreeNode(5)))
solution = Solution()
print(solution.goodNodes(root))

"""
This implementation uses DFS traversal to keep track of the max value so far.
We pass the max value down with the nodes so every node have the max value of its path too.
If the current node value is more or equal to the max of its path, we add one to the count and make it the new max.
We return the count after the traversal.

Time complexity is O(n) because we visit every node once
Space complexity is O(h) where h is the max height of the tree
"""
