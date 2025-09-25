class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(val) {
    const node = new Node(val);
    if (!this.head) {
      this.head = node;
      this.tail = this.head;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.length++;
    return this;
  }
  pop() {
    if (!this.head) return undefined;
    const popped = this.tail;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = popped.prev;
      this.tail.next = null;
      popped.prev = null;
    }
    this.length--;
    return popped;
  }
  shift() {
    if (this.length === 0) return undefined;
    const oldHead = this.head;
    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = oldHead.next;
      this.head.prev = null;
      oldHead.next = null;
    }
    this.length--;
    return oldHead;
  }
  unShift(val) {
    const newNode = new Node(val);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
    this.length++;
    return this;
  }
  get(i) {
    if (i < 0 || i >= this.length) return null;
    if (i === 0) return this.head;
    if (i === this.length - 1) return this.tail;
    if (i <= this.length / 2) {
      let counter = 1;
      let currentNode = this.head.next;
      while (counter !== i) {
        currentNode = currentNode.next;
        counter++;
      }
      return currentNode;
    } else {
      let counter = this.length - 2;
      let currentNode = this.tail.prev;
      while (counter !== i) {
        currentNode = currentNode.prev;
        counter--;
      }
      return currentNode;
    }
  }
  set(i, val) {
    const found = this.get(i);
    if (found) {
      found.val = val;
      return true;
    }
    return false;
  }
  insert(i, val) {
    if (i < 0 || i >= this.length) return false;
    if (i === 0) return !!this.unShift(val);
    if (i === this.length - 1) return !!this.push(val);

    const newNode = new Node(val);
    const pre = this.get(i - 1);
    const nextNode = pre.next;

    newNode.prev = pre;
    newNode.next = nextNode;
    pre.next = newNode;
    nextNode.prev = newNode;

    this.length++;
    return true;
  }
  remove(i) {
    if (i < 0 || i >= this.length) return undefined;
    if (i === 0) return this.shift();
    if (i === this.length - 1) return this.pop();

    const node = this.get(i);
    const pre = node.prev;
    const next = node.next;
    pre.next = next;
    next.prev = pre;

    node.next = null;
    node.prev = null;

    this.length--;
    return node;
  }
}

const list = new DoublyLinkedList();

list.push(1);
list.push(2);
list.push(3);
console.log(list.remove(1));
console.log(list);
