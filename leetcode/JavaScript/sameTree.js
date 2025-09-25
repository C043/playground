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

const treeOne = new BinaryTree()
const treeTwo = new BinaryTree()
treeOne.insert(1)
treeOne.insert(2)
treeOne.insert(3)
treeTwo.insert(1)
treeTwo.insert(2)
treeTwo.insert(3)

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
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
  if (!p && !q) return true

  const pQueue = [p]
  const qQueue = [q]

  while (pQueue.length > 0 && qQueue.length > 0) {
    const pNode = pQueue.shift()
    const qNode = qQueue.shift()

    if (qNode === null && pNode === null) continue
    if (qNode === null && pNode !== null) return false
    if (qNode !== null && pNode === null) return false

    if (pNode.val !== qNode.val) return false

    pQueue.push(pNode.left)
    pQueue.push(pNode.right)
    qQueue.push(qNode.left)
    qQueue.push(qNode.right)
  }

  return true
}
// @leet end
console.log(isSameTree(treeOne.root, treeTwo.root))
