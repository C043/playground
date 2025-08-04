class CustomQueue {
  constructor() {
    this.length = 0
    this.queue = []
  }

  enqueue(val) {
    this.queue.push(val)
    this.length++
  }

  dequeue() {
    this.length--
    return this.queue.shift()
  }

  includes(val) {
    for (const value of this.queue) {
      if (value === val) {
        return true
      }
    }

    return false
  }
}

export default CustomQueue
