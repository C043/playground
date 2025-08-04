export class UniqueQueue {
  constructor() {
    this.set = new Set()
    this.queue = []
    this.length = 0
  }

  enqueue(val) {
    if (!this.set.has(val)) {
      this.set.add(val)
      this.queue.push(val)
      this.length++
    }
  }

  dequeue() {
    if (this.length > 0) {
      this.length--
      return this.queue.shift()
    }

    return null
  }

  includes(val) {
    return this.set.has(val)
  }
}
