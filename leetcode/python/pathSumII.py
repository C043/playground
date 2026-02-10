from typing import List, Optional
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        listToReturn: List[List[int]] = []
        path: List[int] = []
        stack: List[tuple[TreeNode, int, int]] = [(root, 0, 0)]

        while stack:
            node, depth, runSum = stack.pop()

            if len(path) > depth:
                del path[depth:]

            path.append(node.val)
            runSum += node.val

            if node.right:
                stack.append((node.right, depth + 1, runSum))
            if node.left:
                stack.append((node.left, depth + 1, runSum))

            if not node.left and not node.right:
                if runSum == targetSum:
                    listToReturn.append(path.copy())

        return listToReturn


root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)))))
root = TreeNode(
    5,
    TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))),
)
solution = Solution()
print(solution.pathSum(root, 22))

"""
This solution uses iterative DFS traversal in order to keep track of the current path, the current sum of the path.
When we arrive at a leaf, we append a copy of the current path to the list to return only if the current sum is equal to the target sum.
In order to keep the current path updated, we store in the stack a tuple[TreeNode, depth, currentSum]. We need the depth because when we reach a leaf, we need to backtrack the path to keep it updated.
So what happens is this:
- We pop the next node that has a depth < the depth of the previous leaf
- We slice the path to keep only the current depth path, the depth from the current node
- We keep going

The time complexity is O(n) because we visit each node only once
The space complexity is O(h) because we store at most the max height of the tree
"""
