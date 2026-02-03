from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = []
        stack2 = []
        stack1.append(p)
        stack2.append(q)

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 and not node2 or node2 and not node1:
                return False
            if node1 and node2 and node1.val != node2.val:
                return False

            if node1:
                stack1.append(node1.left)
            if node1:
                stack1.append(node1.right)

            if node2:
                stack2.append(node2.left)
            if node2:
                stack2.append(node2.right)

        if stack1 or stack2:
            return False

        return True


root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(5))

root1 = TreeNode(1, TreeNode(2))
root2 = TreeNode(1, None, TreeNode(2))

solution = Solution()
print(solution.isSameTree(root1, root2))

"""
This implementation uses two stacks to perform a DFS on each tree in order to check if the nodes are equal. If they are not, we return False, if they are equal, we append their left and right nodes to the stacks and we keep going until either we find some nodes that are not equal, or we visit every node and return True because they are the same tree.

The time complexity is O(n) where n is the number of nodes because in the worst case we visit each node once
The space complexity is O(h) where h is the height of the tree
This is because in the worst case, we keep all the trees inside the stacks
"""
