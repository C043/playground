from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        stack: List[tuple[TreeNode, int]] = [(root, 0)]
        result: List[str] = []
        path: List[int] = []

        while stack:
            node, depth = stack.pop()

            if len(path) > depth:
                del path[depth:]
            path.append(node.val)

            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))

            if not node.left and not node.right:
                result.append("->".join(map(str, path)))

        return result


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
solution = Solution()
print(solution.binaryTreePaths(root))
