class WeightedGraph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  addEdge(v1, v2, weight) {
    if (!this.adjacencyList[v1]) this.addVertex(v1);
    if (!this.adjacencyList[v2]) this.addVertex(v2);

    this.adjacencyList[v1].push({
      node: v2,
      weight: weight,
    });
    this.adjacencyList[v2].push({
      node: v1,
      weight: weight,
    });
  }

  removeEdge(v1, v2) {
    this.adjacencyList[v1] = this.adjacencyList[v1].filter(
      (v) => v.node !== v2,
    );
    this.adjacencyList[v2] = this.adjacencyList[v2].filter(
      (v) => v.node !== v1,
    );
  }

  removeVertex(vertex) {
    for (const v in this.adjacencyList) {
      this.removeEdge(vertex, v);
    }
    delete this.adjacencyList[vertex];
  }

  dijkstra(v1, v2) {
    const distances = {};
    const pq = new PriorityQueue();
    const previous = {};
    const path = [];

    for (const vertex in this.adjacencyList) {
      if (vertex === v1) {
        distances[vertex] = 0;
        pq.enqueue(vertex, 0);
      } else {
        distances[vertex] = Infinity;
        pq.enqueue(vertex, Infinity);
      }
      previous[vertex] = null;
    }

    while (pq.values.length) {
      let currentNode = pq.dequeue().val;

      if (currentNode === v2) {
        while (previous[currentNode]) {
          path.push(currentNode);
          currentNode = previous[currentNode];
        }
        break;
      }

      if (currentNode || distances[currentNode] !== Infinity) {
        for (const neighbor in this.adjacencyList[currentNode]) {
          const nextNode = this.adjacencyList[currentNode][neighbor];
          const currentDistance = distances[currentNode] + nextNode.weight;

          if (distances[nextNode.node] > currentDistance) {
            distances[nextNode.node] = currentDistance;
            previous[nextNode.node] = currentNode;
            pq.enqueue(nextNode.node, currentDistance);
          }
        }
      }
    }
    return path.concat(v1).reverse();
  }
}

class SimplePriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    this.values.push({
      val,
      priority,
    });
    this.#sort();
  }

  dequeue() {
    return this.values.shift();
  }

  #sort() {
    this.values.sort((a, b) => a.priority - b.priority);
  }
}

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

const g = new WeightedGraph();

g.addVertex("A");
g.addVertex("B");
g.addVertex("C");
g.addVertex("D");
g.addVertex("E");
g.addVertex("F");

g.addEdge("A", "B", 4);
g.addEdge("A", "C", 2);

g.addEdge("C", "D", 2);
g.addEdge("C", "F", 4);

g.addEdge("D", "F", 1);
g.addEdge("D", "E", 3);

g.addEdge("F", "E", 1);

g.addEdge("E", "B", 3);

console.log(g.dijkstra("F", "E"));
//console.log(g.adjacencyList);
