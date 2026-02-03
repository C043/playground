from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        leftTraverse = []
        rightTraverse = []
        if root.left:
            leftTraverse = self.inorderTraversal(root.left)
        if root.right:
            rightTraverse = self.inorderTraversal(root.right)

        return leftTraverse + [root.val] + rightTraverse


root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
    TreeNode(3, None, TreeNode(8, TreeNode(9))),
)
solution = Solution()
print(solution.inorderTraversal(root))

"""
This implementation uses recursive DFS traversal in order to build and concatenate three arrays.
Every time, we call the method on the left side of the node and on the right side with base case that the node is not None, in that case we return an empty array.
This means that we always do DFS on the left and on the right side of the node and we return the concatenation of the inordered left side + the the root + the inordered right side.
We treat every node as the root in the recursive calls to make the problem smaller.

The time complexity is O(n) because we visit every node once
The space complexity is O(n) because we store every node value in the arrays so the space grows linearly with the nodes
"""
