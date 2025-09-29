// @leet start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  // Return true if the root has no side
  if (!root.left && !root.right) return true
  // Return false if the root has only one side
  if ((!root.left && root.right) || (root.left && !root.right)) return false

  // Create a queue
  // Push the left and right node to the queue
  const leftQueue = [root.left]
  const rightQueue = [root.right]
  // while the queue is not empty, take the first two in line
  // Compare their left and right values
  while (leftQueue.length > 0 && rightQueue.length > 0) {
    const leftNode = leftQueue.pop()
    const rightNode = rightQueue.pop()
    // Compare their values
    if (leftNode && rightNode && leftNode.val === rightNode.val) {
      if (
        leftNode.left &&
        rightNode.right &&
        leftNode.left.val !== rightNode.right.val
      ) {
        return false
      }
      if (
        rightNode.left &&
        leftNode.right &&
        rightNode.left.val !== leftNode.right.val
      ) {
        return false
      }
    } else if (leftNode === rightNode) {
      continue
    } else {
      return false
    }

    // Push their left and right values to the queue
    leftQueue.push(leftNode.left)
    leftQueue.push(leftNode.right)
    rightQueue.push(rightNode.right)
    rightQueue.push(rightNode.left)
  }

  return true
}
// @leet end
