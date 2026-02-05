from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None

        rootIndex = inorder.index(preorder[0])

        inorderLeft = inorder[:rootIndex]
        inorderRight = inorder[rootIndex + 1 :]

        preorderLeft = preorder[1 : len(inorderLeft) + 1]
        preorderRight = preorder[len(inorderLeft) + 1 :]

        root = TreeNode(
            preorder[0],
            self.buildTree(preorderLeft, inorderLeft),
            self.buildTree(preorderRight, inorderRight),
        )

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
solution = Solution()
print(solution.buildTree(preorder, inorder))
