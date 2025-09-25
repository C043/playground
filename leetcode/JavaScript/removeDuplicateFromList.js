class Node {
  constructor(val) {
    this.val = val
    this.next = null
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null
    this.tail = null
    this.length = 0
  }
  push(val) {
    const node = new Node(val)
    if (!this.head) {
      this.head = node
      this.tail = node
    } else {
      this.tail.next = node
      this.tail = node
    }
    this.length += 1
    return this
  }
  pop() {
    if (!this.head) return undefined
    let current = this.head
    let pre = null
    while (current.next) {
      pre = current
      current = pre.next
    }
    this.length--
    if (this.length === 0) {
      this.head = null
      this.tail = null
    } else {
      pre.next = null
      this.tail = pre
    }
    return current
  }
  shift() {
    if (!this.head) return undefined
    const oldHeadNode = this.head
    this.head = oldHeadNode.next
    oldHeadNode.next = null
    this.length--
    if (this.length === 0) this.tail = null
    return oldHeadNode
  }
  unShift(val) {
    const node = new Node(val)
    if (!this.head) {
      this.head = node
      this.tail = node
    } else {
      node.next = this.head
      this.head = node
    }
    this.length++
    return this
  }
  get(i) {
    if (i < 0 || i >= this.length) return null
    let current = this.head
    for (let j = 0; j < i; j++) {
      current = current.next
    }
    return current
  }
  set(i, val) {
    const node = this.get(i)
    if (node) {
      node.val = val
      return true
    }
    return false
  }
  insert(i, val) {
    if (i < 0 || i > this.length) return false
    if (i === 0) return !!this.unShift(val)
    if (i === this.length) return !!this.push(val)
    const node = new Node(val)
    const pre = this.get(i - 1)
    const next = pre.next
    node.next = next
    pre.next = node
    this.length++
    return true
  }
  remove(i) {
    if (i < 0 || i > this.length) return undefined
    if (i === this.length - 1) return this.pop()
    if (i === 0) return this.shift()
    const pre = this.get(i - 1)
    const removedNode = pre.next
    pre.next = removedNode.next
    removedNode.next = null
    this.length--
    return removedNode
  }
  reverse() {
    let node = this.head
    this.head = this.tail
    this.tail = node
    let next = null
    let pre = null
    for (let i = 0; i < this.length; i++) {
      next = node.next
      node.next = pre
      pre = node
      node = next
    }
    return this
  }
}

const list = new SinglyLinkedList()
list.push(1)
list.push(1)
list.push(1)
list.push(2)
list.push(2)
list.push(2)
list.push(3)
list.push(3)
// @leet start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  if (!head) return head
  let previousNode = head
  while (previousNode.next !== null) {
    if (previousNode.val === previousNode.next.val) {
      previousNode.next = previousNode.next.next
    } else {
      previousNode = previousNode.next
    }
  }
  return head
}
// @leet end

console.log(deleteDuplicates(list.head))
