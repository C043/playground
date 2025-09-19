class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  addEdge(v1, v2) {
    if (!this.adjacencyList[v1]) this.addVertex(v1);
    if (!this.adjacencyList[v2]) this.addVertex(v2);
    this.adjacencyList[v1].push(v2);
    this.adjacencyList[v2].push(v1);
  }

  removeEdge(v1, v2) {
    this.adjacencyList[v1] = this.adjacencyList[v1].filter((v) => v !== v2);
    this.adjacencyList[v2] = this.adjacencyList[v2].filter((v) => v !== v1);
  }

  removeVertex(vertex) {
    for (const v in this.adjacencyList) {
      this.removeEdge(vertex, v);
    }
    delete this.adjacencyList[vertex];
  }

  DFTRecursive(vertex) {
    const result = [];
    const visited = new Set();
    const adjacencyList = this.adjacencyList;

    (function DFT(v) {
      if (adjacencyList[v].length === 0) return;
      result.push(v);
      visited.add(v);
      for (const neighbor of adjacencyList[v]) {
        if (!visited.has(neighbor)) DFT(neighbor);
      }
    })(vertex);

    return result;
  }

  DFTIteratively(vertex) {
    const stack = [vertex];
    const visited = new Set();
    const result = [];

    while (stack.length) {
      const currentVertex = stack.pop();
      if (!visited.has(currentVertex)) {
        result.push(currentVertex);
        visited.add(currentVertex);
        this.adjacencyList[currentVertex].forEach((element) => {
          stack.push(element);
        });
      }
    }

    return result;
  }

  BFT(vertex) {
    const queue = [vertex];
    const visited = new Set();
    while (queue.length) {
      const currentVertex = queue.shift();
      visited.add(currentVertex);
      this.adjacencyList[currentVertex].forEach((element) => {
        if (!visited.has(element)) {
          queue.push(element);
        }
      });
    }
    return Array.from(visited);
  }
}

const g = new Graph();
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");
g.addVertex("D");
g.addVertex("E");
g.addVertex("F");

g.addEdge("A", "B");
g.addEdge("A", "C");
g.addEdge("B", "D");
g.addEdge("C", "E");
g.addEdge("D", "E");
g.addEdge("D", "F");
g.addEdge("E", "F");
console.log(g.DFTRecursive("A"));
console.log(g.DFTIteratively("A"));
console.log(g.BFT("A"));
console.log(g.adjacencyList);
