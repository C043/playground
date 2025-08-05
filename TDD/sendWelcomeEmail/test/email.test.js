import assert from "assert"
import sinon from "sinon"
import { sendWelcomeEmail } from "../email.js"

describe("sendWelcomeEmail", () => {
  let emailService

  beforeEach(() => {
    emailService = { send: sinon.fake() }
  })

  it("should call emailService.send with correct args", () => {
    const user = { name: "Alice", email: "alice@example.com" }

    sendWelcomeEmail(user, emailService)

    assert.strictEqual(emailService.send.calledOnce, true)
    assert.strictEqual(
      emailService.send.calledWithMatch({
        to: "alice@example.com",
        subject: "Welcome!",
        body: "Hello, Alice!"
      }),
      true
    )
  })

  it("should throw if user has no email", () => {
    const user = { name: "Bob" }

    assert.throws(() => sendWelcomeEmail(user, emailService), {
      name: "Error",
      message: "No Email provided"
    })
  })
})
