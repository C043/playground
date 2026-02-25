from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack: List[tuple[TreeNode, bool]] = [(root, False)]
        result = 0

        while stack:
            node, left = stack.pop()

            if left and not node.left and not node.right:
                result += node.val

            if node.left:
                stack.append((node.left, True))

            if node.right:
                stack.append((node.right, False))

        return result


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.sumOfLeftLeaves(root))

"""
This solution uses DFS tree traversal and keeps track if the node is left or right.
When we arrive to a leave and it's left, we sum its value to the result.
We return the result when the traversal is over.

Time complexity is O(n) because we visit every node once
Space complexity is O(h) where h is the max height of the tree
"""
