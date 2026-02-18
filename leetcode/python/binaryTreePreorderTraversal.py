from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result: List[int] = []
        stack: List[TreeNode] = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
    TreeNode(3, None, TreeNode(8, TreeNode(9))),
)
solution = Solution()
print(solution.preorderTraversal(root))

"""
This solution is fairly simple:
We traverse the tree using DFS from left to right and we add every value to a list that we return in the end.

Time complexity is O(n) because we visit every node once
Space complexity is O(h) where h is the max heigth of the tree
"""
