class MaxBinaryHeap {
  constructor(array = []) {
    this.values = array;
  }

  insert(val) {
    this.values.push(val);
    this.#bubbleUp();
  }

  extractTop() {
    if (this.values.length === 0) return null;
    this.#swap(0, this.values.length - 1);
    const maxValue = this.values.pop();
    this.#bubbleDown();

    return maxValue;
  }

  #bubbleUp() {
    let index = this.values.length - 1;
    let parentIndex = Math.floor((index - 1) / 2);

    while (this.values[parentIndex] < this.values[index]) {
      this.#swap(index, parentIndex);
      index = parentIndex;
      parentIndex = Math.floor((index - 1) / 2);
    }
  }

  #bubbleDown() {
    let parentIndex = 0;
    const length = this.values.length;
    let leftChild = this.values[parentIndex * 2 + 1];
    let rightChild = this.values[parentIndex * 2 + 2];

    while (
      this.values[parentIndex] < leftChild ||
      this.values[parentIndex] < rightChild
    ) {
      if (length === 2) {
        this.#swap(0, 1);
        break;
      } else {
        const maxChildIndex =
          Math.max(leftChild, rightChild) === leftChild
            ? parentIndex * 2 + 1
            : parentIndex * 2 + 2;
        this.#swap(parentIndex, maxChildIndex);
        parentIndex = maxChildIndex;
        leftChild = this.values[parentIndex * 2 + 1];
        rightChild = this.values[parentIndex * 2 + 2];
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

class MinBinaryHeap {
  constructor() {
    this.values = [];
  }

  insert(val) {
    this.values.push(val);
    this.#bubbleUp();
  }

  extractTop() {
    if (this.values.length === 0) return undefined;
    this.#swap(0, this.values.length - 1);
    const minValue = this.values.pop();
    this.#bubbleDown();

    return minValue;
  }

  #bubbleUp() {
    let index = this.values.length - 1;
    let parentIndex = Math.floor((index - 1) / 2);

    while (this.values[parentIndex] > this.values[index]) {
      this.#swap(index, parentIndex);
      index = parentIndex;
      parentIndex = Math.floor((index - 1) / 2);
    }
  }

  #bubbleDown() {
    let parentIndex = 0;
    const length = this.values.length;
    let leftChild = this.values[parentIndex * 2 + 1];
    let rightChild = this.values[parentIndex * 2 + 2];

    while (
      this.values[parentIndex] > leftChild ||
      this.values[parentIndex] > rightChild
    ) {
      if (length === 2) {
        this.#swap(0, 1);
        break;
      } else {
        const minChildIndex =
          Math.min(leftChild, rightChild) === leftChild
            ? parentIndex * 2 + 1
            : parentIndex * 2 + 2;
        this.#swap(parentIndex, minChildIndex);
        parentIndex = minChildIndex;
        leftChild = this.values[parentIndex * 2 + 1];
        rightChild = this.values[parentIndex * 2 + 2];
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

const heap = new MinBinaryHeap();
heap.insert(1);
console.log(heap.values);
