class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
  push(val) {
    const newNode = new Node(val);
    if (this.size === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      const oldFirst = this.first;
      this.first = newNode;
      this.first.next = oldFirst;
    }
    return ++this.size;
  }
  pop() {
    if (this.size === 0) return null;
    const oldFirst = this.first;
    if (this.first === this.last) this.last = null;
    this.first = this.first.next;
    this.size--;
    oldFirst.next = null;
    return oldFirst;
  }
}

const stack = new Stack();

console.log(stack.push(4));
console.log(stack.pop());
console.log(stack);
