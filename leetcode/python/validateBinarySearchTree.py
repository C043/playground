from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
    ) -> bool:
        if not root:
            return True

        return self.check(root, float("-inf"), float("inf"))

    def check(self, root: Optional[TreeNode], low: float, high: float) -> bool:
        if not root:
            return True
        if not (low < root.val < high):
            return False
        return self.check(root.left, low, root.val) and self.check(
            root.right, root.val, high
        )


root = TreeNode(45, TreeNode(42, None, TreeNode(44, TreeNode(43, TreeNode(41)))))
root = TreeNode(2, TreeNode(2), TreeNode(2))
root = TreeNode(2, TreeNode(1), TreeNode(3))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
root = TreeNode(
    3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6))
)
solution = Solution()
print(solution.isValidBST(root))

"""
This implementation uses recursive DFS to check at every node if the node is within the low and high constraints.
The constraints change dynamically based on whether we're going left or right.
If we're going left, the new high constraint is the current node value.
This is because when we left subtrees cannot be higher than any node on upper level on their right.
If we're going right, the new low constraint is the current node value.
This is because when we right subtrees cannot be lower than any node on upper level on their left.

Constraints are kept between function calls to preserve the right constraints at every call and update the ones that needs updating.

The base recursive case is that we pass None to the function.
When this happens, we return True because it means that we reached the end of the left or right subtree and it's valid until this point.

At the end, if every recursive call returns True, tree is a valid BST.

The time complexity is O(n) because we visit each node once
The space complexity is O(h) where h is the height of the tree due to the recursion nature of the algorithm
"""
