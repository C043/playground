from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return root.val

        return self.traverse(root.left, root.val) + self.traverse(root.right, root.val)

    def traverse(self, root: Optional[TreeNode], compiledNum: int) -> int:
        if not root:
            return 0
        if root and not root.left and not root.right:
            return int(str(compiledNum) + str(root.val))

        compiledNum = int(str(compiledNum) + str(root.val))

        return self.traverse(root.left, compiledNum) + self.traverse(
            root.right, compiledNum
        )


root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.sumNumbers(root))

"""
This solution uses a recursive DFS helper function to compile the numbers to sum.
The recursive base cases are two:
- There is no node: in that case, we return 0
- We arrived to a leafe: we return the compiled number

Otherwise we compile the number and we call the helper function on the left and right node with the new compiled number, summing the results.

This compile every number from the root to every leaf and sums them.

The time complexity is O(n) as we traverse all the tree once
The space complexity is O(1) if we do not count the call stack
If we count the call stack, then it's O(h) where h is the height of the tree (O(n) on a skewed tree)
"""
