from typing import Optional

from TreeNode import TreeNode
from collections import deque


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []

        def explore(node: Optional[TreeNode], path: list[str]) -> None:
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                explore(node.left, path)
                explore(node.right, path)

            path.pop()

        explore(root, [])
        return result


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.binaryTreePaths(root))
