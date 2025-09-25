const util = require("util");

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(val) {
    const newNode = new Node(val);
    if (!this.root) {
      this.root = newNode;
      return this;
    }
    try {
      let currentNode = this.root;
      while (true) {
        if (val === currentNode.val) throw new Error("Node already present");
        if (val < currentNode.val) {
          if (!currentNode.left) {
            currentNode.left = newNode;
            return this;
          }
          currentNode = currentNode.left;
        } else if (val > currentNode.val) {
          if (!currentNode.right) {
            currentNode.right = newNode;
            return this;
          }
          currentNode = currentNode.right;
        }
      }
    } catch (e) {
      console.log(e.message);
    }
  }
  contains(val) {
    if (!this.root) return false;
    let currentNode = this.root;
    let found = false;
    while (currentNode && !found) {
      if (val < currentNode.val) {
        currentNode = currentNode.left;
      } else if (val > currentNode.val) {
        currentNode = currentNode.right;
      } else {
        found = true;
      }
    }
    return found;
  }
}

const tree = new BinarySearchTree();

tree.insert(1);
tree.insert(2);
tree.insert(0);
tree.insert(3);
tree.insert(5);
console.log(util.inspect(tree, { depth: null, colors: true }));
console.log(tree.contains(10));
