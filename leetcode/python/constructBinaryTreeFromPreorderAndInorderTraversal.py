from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
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

"""
In this problem we need to construct a binary tree using its postorder and inorder array.
postorder = [root, left, right]
inorder = [left, root, right]

We use a recursive DFS function to solve this problem.
The base idea is to return each node and calculate its left and its right by calling the same function with preorder and postorder array for the left subtree and for the right one.

We calculate them by finding the root in the inorder subtree.
We know that the root is the first element in the postorder one.
Then we know the length of the left and right subtrees because they are the elements to the left and to the right of the root in the inorder array.
So we can use it to separate the left from the right subree in the postorder too.
We create a TreeNode with the value from the root, recursion with the left postorder and inorder for the left node, and the same thing for the right but with right postorder and inorder arrays.

We return this node (that will be the root of the tree in the end).
The recursive base case is that there are no elements in the preorder or in the inorder array. In that case we're return None because that will mean that we arrived to a leaf.
"""
