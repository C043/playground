import assert from "assert"
import { UniqueQueue } from "../UniqueQueue.js"

describe("UniqueQueue", () => {
  let uniqueQueue

  beforeEach(() => {
    uniqueQueue = new UniqueQueue()
  })

  it("enqueue two of the same values should only add one to the queue", () => {
    uniqueQueue.enqueue("value")
    uniqueQueue.enqueue("value")

    assert.strictEqual(uniqueQueue.length, 1)
  })

  it("dequeue method should return the first value queued", () => {
    uniqueQueue.enqueue("value1")
    uniqueQueue.enqueue("value2")

    const value = uniqueQueue.dequeue()

    assert.strictEqual(value, "value1")
  })

  it("dequeue method should reduce queue length", () => {
    uniqueQueue.enqueue("value")

    assert.strictEqual(uniqueQueue.length, 1)

    uniqueQueue.dequeue()

    assert.strictEqual(uniqueQueue.length, 0)
  })

  it("dequeue method should return null if queue is empty", () => {
    const value = uniqueQueue.dequeue()
    assert.strictEqual(value, null)
  })

  it("includes method should return true if value is present in the unique queue", () => {
    uniqueQueue.enqueue("value")
    const isIncluded = uniqueQueue.includes("value")

    assert.strictEqual(isIncluded, true)
  })
})
