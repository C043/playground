from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False

        result = False
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()

            result = self.isSameTree(node, subRoot)
            if result:
                return True

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        elif not a or not b:
            return False

        if a.val != b.val:
            return False

        return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)


root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
solution = Solution()
print(solution.isSubtree(root, subRoot))

"""
This solution checks if at every node if that node and all its descendants are the same as the subRoot.
It does so with a DFS tree traversal where every node it invokes the isSameTree method on the current node with the subRoot.
The isSameTree method returns True if and only if the subtree is equal, False otherwise.
If it returns True, we return True, otherwise we keep traversing.

Time complexity is O(n2) because we're checking every node of subRoot with every node of root
Space complexity is O(h) for the stack and for the recursive calls
"""
