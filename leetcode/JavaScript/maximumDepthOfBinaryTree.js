class Node {
  constructor(val) {
    this.val = val
    this.left = null
    this.right = null
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null
  }
  insert(val) {
    const newNode = new Node(val)
    if (!this.root) {
      this.root = newNode
      return this
    }
    try {
      let currentNode = this.root
      while (true) {
        if (val === currentNode.val) throw new Error("Node already present")
        if (val < currentNode.val) {
          if (!currentNode.left) {
            currentNode.left = newNode
            return this
          }
          currentNode = currentNode.left
        } else if (val > currentNode.val) {
          if (!currentNode.right) {
            currentNode.right = newNode
            return this
          }
          currentNode = currentNode.right
        }
      }
    } catch (e) {
      console.log(e.message)
    }
  }
  contains(val) {
    if (!this.root) return false
    let currentNode = this.root
    let found = false
    while (currentNode && !found) {
      if (val < currentNode.val) {
        currentNode = currentNode.left
      } else if (val > currentNode.val) {
        currentNode = currentNode.right
      } else {
        found = true
      }
    }
    return found
  }
}

const tree = new BinarySearchTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)

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
 * @return {number}
 */
var maxDepth = function (root) {
  if (!root) return 0
  if (!root.left && !root.right) return 1

  let max = 0

  let queue = [root]

  while (queue.length > 0) {
    const subQueue = queue
    queue = []
    while (subQueue.length > 0) {
      const currentNode = subQueue.shift()
      if (currentNode.left) queue.push(currentNode.left)
      if (currentNode.right) queue.push(currentNode.right)
    }
    max++
  }

  return max
}
// @leet end

console.log(maxDepth(tree.root))
