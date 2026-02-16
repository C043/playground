from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxResult = float("-inf")

        stack: List[tuple[TreeNode, int]] = [(root, 0)]
        path: List[int] = []

        while stack:
            node, depth = stack.pop()

            if len(path) > depth:
                del path[depth:]

            path.append(node.val)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

            if not node.right and not node.left:
                maxResult = max(max(path) - min(path), maxResult)

        return int(maxResult)


root = TreeNode(
    8,
    TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
    TreeNode(10, None, TreeNode(14, TreeNode(13))),
)
root = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3))))
solution = Solution()
print(solution.maxAncestorDiff(root))

"""
This solution uses a DFS tree traversal in order to keep track of the current path and when we arrive to a leaf, we try to subtract the min value of the path from its max one.
We assign it to the maxResult we'll be returning in the end if its greater than the current one.

Time complexity is O(n) because we visit each node of the tree once
Space complexity is O(h) because we store in the worst case the max height of the tree in the stack
"""
