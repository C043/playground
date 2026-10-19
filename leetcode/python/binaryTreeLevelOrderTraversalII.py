from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            currentLevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                currentLevel.append(node.val)

                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)

            levels.append(currentLevel)

        return levels[::-1]


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
solution = Solution()
print(solution.levelOrderBottom(root))
