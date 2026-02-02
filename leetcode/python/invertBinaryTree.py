from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        currentLeft = root.left
        currentRight = root.right
        root.right = currentLeft
        root.left = currentRight

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


root = TreeNode(
    4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
)
solution = Solution()
print(solution.invertTree(root).left.left.val)

"""
This implementation uses DFS to invert a binary tree.
We use recursion to do this.
The recursion base case is that the root is None.
We invert root's left and right.
We call the same method on root's left and on root's right.
We return root.

The time complexity is O(n) because we visit each node exactly once
The space complexity is O(1) if we're not counting the call stack.
In that case the space complexity is O(n) because we call the method on every node.
It's O(log n) on a balanced binary tree because the call stack at each step contains double the number of calls it has in the previous step. This means that to cover n nodes you only need about log2(n) levels, so the maximum call stack depth is log2(n).
"""
