from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            node.right = stack[-1] if stack else None
            node.left = None


root = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))
)
solution = Solution()
print(solution.flatten(root))

"""
In this solution, we use a iterative DFS to traverse the tree and assigning to each node, the next element in the stack (without popping it). We also assign its left to None.
This works because using a stack in DFS puts the nodes in the correct postorder.

The time complexity is O(n) because we visit each node of the tree once
The space complexity is O(h) where h is the height of the tree
"""
