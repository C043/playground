from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue: deque[TreeNode] = deque([root])
        result: List[List[int]] = []
        left = True

        while queue:
            level = len(queue)
            levelVals: List[int] = []

            for i in range(level):
                node = queue.popleft()
                levelVals.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left:
                levelVals.reverse()
            left = not left
            result.append(levelVals)
        return result
      def zigzagLevelOrderBetter(self, root: Optional[TreeNode]) -> List[List[int]]:
          if not root:
              return []

          q = deque([root])
          res: List[List[int]] = []
          left_to_right = True

          while q:
              level_size = len(q)
              level_vals = deque()

              for _ in range(level_size):
                  node = q.popleft()
                  if left_to_right:
                      level_vals.append(node.val)
                  else:
                      level_vals.appendleft(node.val)

                  if node.left:
                      q.append(node.left)
                  if node.right:
                      q.append(node.right)

              res.append(list(level_vals))
              left_to_right = not left_to_right

          return res


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
solution = Solution()
print(solution.zigzagLevelOrder(root))

"""
In this implementation we use BFS tree traversal and keep track of the level values. We reverse them if the variable "left" is False.
Then we append the level values to the result list.
In the end, we return the result list.

There is a better version that does not require reverse method which is another O(n).
In this better version, we insert to the left or to the right of the level values list based on the "left" variable.
This way we don't need to reverse. To do this, we need to use a deque for the level values too.

Time complexity is O(n) because we traverse all the nodes once
Space complexity is O(w) because we keep saved in the queue max tree width at most
"""
