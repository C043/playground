from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif not root.left and root.right or not root.right and root.left:
            return False

        return self.check(root.left, root.right)

    def check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        leftTraversal = True
        rightTraversal = True

        if not left and right or not right and left:
            return False
        elif right and left and right.val != left.val:
            return False
        elif left and right and left.val == right.val:
            leftTraversal = self.check(left.left, right.right)
            rightTraversal = self.check(left.right, right.left)

        return leftTraversal and rightTraversal


root = TreeNode(
    5,
    TreeNode(2, TreeNode(4, None, TreeNode(1))),
    TreeNode(2, None, TreeNode(1, TreeNode(2))),
)
root = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
)
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
solution = Solution()
print(solution.isSymmetric(root))

"""
This implementation uses recursive DFS in order to check the symmetry of a binary tree.
We create a helper method that checks if two nodes have the same value. If so, it calls itself on left.left with right.right and with left.right with right.left to check the keep checking the symmetry down the tree.
If any one of these return False, it means that the tree is not symmetric and we return false.

The time complexity is O(n) where n the number of nodes in the tree (we visit them all once in the worst case)
The space complexity is O(h) where h is the height of the tree
"""
