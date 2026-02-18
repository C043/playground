from typing import List, Optional
import heapq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        stack: List[TreeNode] = []
        curr: TreeNode | None = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

        return 0

    def kthSmallestUnoptized(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        result = 0
        stack: List[TreeNode] = [root]
        minHeap = []

        while stack:
            node = stack.pop()

            heapq.heappush(minHeap, node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        for i in range(k):
            result = heapq.heappop(minHeap)

        return result


root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
solution = Solution()
print(solution.kthSmallest(root, 3))

"""
My unoptimized solution is to traverse all the tree doing DFS and storing each value in a min heap.
Then popping for k times to return the result.
This is not optimal because:
- We traverse all the tree even though we don't need to
- We store all the tree in the heap

The optimized solution is to go immediately to the far left of the tree putting all the nodes we encounter on the way there in the stack.
Then popping and reducing k by one.
If the left subtree is not enough for k, then we visit the right subtree.
When k is equal to 0, it means that we're in the correct node and we return its value.

This implementation is O(n) in the worst case because it's not necessary to visit every node, but it can happen on certain trees and with certain k values
Space complexity is O(h) because we keep in memory the max height of the tree
"""
