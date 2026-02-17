from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        if not root:
            return []

        stack: List[TreeNode] = [root]
        result: List[int] = []
        i = 0

        if root.val != voyage[0]:
            return [-1]

        while stack:
            i += 1
            node = stack.pop()

            if node.left and voyage[i] != node.left.val:
                node.left, node.right = node.right, node.left
                result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result


root = TreeNode(1, TreeNode(2))
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.flipMatchVoyage(root, [1, 3, 2]))
