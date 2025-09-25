class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    const newNode = new Node(val, priority);
    this.values.push(newNode);
    if (this.values.length > 1) this.#bubbleUp();
  }

  #bubbleUp() {
    if (this.values.length === 1) return;
    let index = this.values.length - 1;
    let parentIndex = Math.floor((index - 1) / 2);

    while (this.values[parentIndex].priority > this.values[index].priority) {
      this.#swap(index, parentIndex);
      index = parentIndex;
      parentIndex = Math.floor((index - 1) / 2);
      if (parentIndex < 0) break;
    }
  }

  dequeue() {
    if (this.values.length === 0) return null;
    this.#swap(0, this.values.length - 1);
    const minValue = this.values.pop();
    if (this.values.length > 1) this.#bubbleDown();

    return minValue;
  }

  #bubbleDown() {
    let parentIndex = 0;
    const length = this.values.length;
    let leftChild = this.values[parentIndex * 2 + 1];

    if (length > 2) {
      let rightChild = this.values[parentIndex * 2 + 2];
      while (
        this.values[parentIndex].priority > leftChild.priority ||
        this.values[parentIndex].priority > rightChild.priority
      ) {
        const minChildIndex =
          Math.min(leftChild.priority, rightChild.priority) ===
          leftChild.priority
            ? parentIndex * 2 + 1
            : parentIndex * 2 + 2;
        this.#swap(parentIndex, minChildIndex);
        parentIndex = minChildIndex;
        leftChild = this.values[parentIndex * 2 + 1];
        rightChild = this.values[parentIndex * 2 + 2];
      }
    } else {
      if (this.values[parentIndex].priority > leftChild.priority) {
        this.#swap(0, 1);
      }
    }
  }

  traversal() {
    for (const [i, val] of this.values.entries()) {
      console.log("Parent:", this.values[i]);
      console.log("Children L:", this.values[i * 2 + 1]);
      console.log("Children R:", this.values[i * 2 + 2]);
    }
  }

  #swap(i, j) {
    [this.values[j], this.values[i]] = [this.values[i], this.values[j]];
  }
}

const priorityQueue = new PriorityQueue();

priorityQueue.enqueue("Taking out the trash", 5);
priorityQueue.enqueue("Tidy your room", 4);
priorityQueue.enqueue("Monitor calibration", 10);
console.log(priorityQueue.dequeue());
console.log(priorityQueue.dequeue());
console.log(priorityQueue.dequeue());
console.log(priorityQueue.dequeue());
console.log(priorityQueue.values);
