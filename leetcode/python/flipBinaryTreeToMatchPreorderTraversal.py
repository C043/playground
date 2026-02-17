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

        while stack:
            node = stack.pop()

            if node.val != voyage[i]:
                return [-1]
            i += 1

            left = node.left
            right = node.right

            if left and i < len(voyage) and left.val != voyage[i]:
                if right and right.val == voyage[i]:
                    result.append(node.val)
                    if left:
                        stack.append(left)
                    if right:
                        stack.append(right)
                else:
                    return [-1]
            else:
                if right:
                    stack.append(right)
                if left:
                    stack.append(left)

        return result


root = TreeNode(1, TreeNode(2))
root = TreeNode(1, TreeNode(2), TreeNode(3))
solution = Solution()
print(solution.flipMatchVoyage(root, [1, 3, 2]))

"""
This solution used DFS traversal in order to visit every node of the tree.
For every node, if the node does not match the current element in the preorder tree traversal, we return -1 because it means that it's not possible to have the same tree as the preorder traversal.
Then we check the next element in the preorder traversal.
If left exist and the element is inside the voyage list boundary and the value of left is not equal to the element we're checking and exist right and the value of right is equal to the element we're checking:
We append the current node value to the result because we would need to swap its children in order to match the postorder list.
Then we append to the stack the left and then right nodes because it's like if we swapped them.
If right is not equal the element we're checking it means that it's not possible to have the same tree as the postorder traversal, so we return -1.
If everything is okay with the left instead, we keep going like nothing happened.

After the traversal, we return the result list.

Time complexity is O(n) because we visit every node once
Space complexity is O(h) as we keep in memory at worst the max height of the tree
"""
