from TreeNode import TreeNode
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        queue = deque([root])
        levels = 0

        while queue:
            level = len(queue)
            levels += 1

            for i in range(level):
                node = queue.popleft()

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)

        return levels


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
solution = Solution()
print(solution.maxDepth(root))
