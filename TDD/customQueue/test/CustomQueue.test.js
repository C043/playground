import assert from "assert"
import CustomQueue from "../CustomQueue.js"
import { beforeEach, describe } from "mocha"

describe("CustomQueue", () => {
  let customQueue

  beforeEach(() => {
    customQueue = new CustomQueue()
  })

  it("enqueue should add the value to the queue", () => {
    assert.strictEqual(customQueue.length, 0)

    customQueue.enqueue("test")

    assert.strictEqual(customQueue.length, 1)
  })

  it("dequeue should pull the first value of the queue", () => {
    assert.strictEqual(customQueue.length, 0)

    customQueue.enqueue("value1")
    customQueue.enqueue("value2")
    customQueue.enqueue("value3")

    assert.strictEqual(customQueue.length, 3)

    const value = customQueue.dequeue()

    assert.strictEqual(value, "value1")
    assert.strictEqual(customQueue.length, 2)
  })

  it("includes method should return true if value is in queue", () => {
    customQueue.enqueue("value")
    assert.strictEqual(customQueue.includes("value"), true)
  })

  it("includes method should return false if value is not in queue", () => {
    customQueue.enqueue("value")
    assert.strictEqual(customQueue.includes("not in queue"), false)
  })
})
