const util = require("util");

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinaryTree {
  constructor() {
    this.root = null;
  }
  insert(val) {
    const newNode = new Node(val);
    if (!this.root) {
      this.root = newNode;
      return this;
    } else {
      let currentNode = this.root;
      while (true) {
        if (!currentNode.left) {
          currentNode.left = newNode;
          return this;
        } else if (!currentNode.right) {
          currentNode.right = newNode;
          return this;
        } else {
          currentNode = val < 0 ? currentNode.left : currentNode.right;
        }
      }
    }
  }
}

const breathFirstSearch = (tree) => {
  const queue = [tree.root];
  const visited = [];

  while (queue.length > 0) {
    const currentNode = queue.shift();
    visited.push(currentNode.val);
    if (currentNode.left) queue.push(currentNode.left);
    if (currentNode.right) queue.push(currentNode.right);
  }

  return visited;
};

// Depth First Search
const preOrder = (tree) => {
  const visited = [];

  function traverse(node) {
    visited.push(node.val);
    if (node.left) traverse(node.left);
    if (node.right) traverse(node.right);
  }
  traverse(tree.root);

  return visited;
};

const postOrder = (tree) => {
  const visited = [];

  function traverse(node) {
    if (node.left) traverse(node.left);
    if (node.right) traverse(node.right);
    visited.push(node.val);
  }
  traverse(tree.root);

  return visited;
};

const inOrder = (tree) => {
  const visited = [];

  function traverse(node) {
    if (node.left) traverse(node.left);
    visited.push(node.val);
    if (node.right) traverse(node.right);
  }
  traverse(tree.root);

  return visited;
};

const tree = new BinaryTree();
tree.insert(0);
tree.insert(-5);
tree.insert(5);
tree.insert(-7);
tree.insert(8);

console.log(util.inspect(tree, { depth: null, colors: true }));
console.log(inOrder(tree));
