from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack: List[tuple[TreeNode, int]] = [(root, 0)]
        result = 0

        while stack:
            node, curr = stack.pop()
            curr = curr * 2 + node.val

            if node.right:
                stack.append((node.right, curr))
            if node.left:
                stack.append((node.left, curr))

            if not node.left and not node.right:
                result += curr

        return result


root = TreeNode(
    1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1))
)
solution = Solution()
print(solution.sumRootToLeaf(root))

"""
This solution uses DFS traversal to sum binary numbers and converting them to decimal system at the same time.
When we arrive to a leaf, we add the current converted binary number to the result.

At the end of the traversal we return the result.

Time complexity is O(n) because we traverse each node once
Space complexity is O(h) because we keep in the stack the max height of the tree
"""
