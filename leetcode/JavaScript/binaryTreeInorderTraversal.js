class Node {
  constructor(val) {
    this.val = val
    this.left = null
    this.right = null
  }
}

class BinaryTree {
  constructor() {
    this.root = null
  }
  insert(val) {
    const newNode = new Node(val)
    if (!this.root) {
      this.root = newNode
      return this
    } else {
      let currentNode = this.root
      while (true) {
        if (!currentNode.left) {
          currentNode.left = newNode
          return this
        } else if (!currentNode.right) {
          currentNode.right = newNode
          return this
        } else {
          currentNode = val < 0 ? currentNode.left : currentNode.right
        }
      }
    }
  }
}

const tree = new BinaryTree()
tree.insert(2)
tree.insert(1)
tree.insert(3)

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
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  const visited = []
  function traverse(node) {
    if (node === null) return
    if (node.left) traverse(node.left)
    visited.push(node.val)
    if (node.right) traverse(node.right)
  }
  traverse(root)
  return visited
}
// @leet end

console.log(inorderTraversal(tree.root))
