import request from "supertest"
import sinon from "sinon"
import assert from "assert"
import { createApp } from "../app.js"

describe("User routes", () => {
  let db
  let app
  const TOKEN = "test-token"

  beforeEach(() => {
    db = {
      getUserById: sinon.stub(),
      createUser: sinon.stub()
    }

    app = createApp(db, TOKEN)
  })

  it("GET /users/:id - should return user if authenticated", async () => {
    const fakeUser = { id: "1", name: "Alice" }
    db.getUserById.resolves(fakeUser)

    const res = await request(app)
      .get("/users/1")
      .set("Authorization", `Bearer ${TOKEN}`)

    assert.strictEqual(res.status, 200)
    assert.deepStrictEqual(res.body, fakeUser)
    assert.ok(db.getUserById.calledOnceWith("1"))
  })

  it("GET /users/:id - should return 401 if token is missing", async () => {
    const res = await request(app).get("/users/1")
    assert.strictEqual(res.status, 401)
    assert.deepStrictEqual(res.body, { error: "Unauthorized" })
  })

  it("GET /users/:id should return 404 if user not found", async () => {
    db.getUserById.resolves(null)

    const res = await request(app)
      .get("/users/2")
      .set("Authorization", `Bearer ${TOKEN}`)

    assert.strictEqual(res.status, 404)
    assert.deepStrictEqual(res.body, { error: "User not found" })
    assert.ok(db.getUserById.calledWith("2"))
  })

  it("POST /users - should create a user if authenticated", async () => {
    const newUser = { id: "2", name: "Bob", email: "bob@example.com" }
    db.createUser.resolves(newUser)

    const res = await request(app)
      .post("/users")
      .set("Authorization", `Bearer ${TOKEN}`)
      .send({ name: "Bob", email: "bob@example.com" })

    assert.strictEqual(res.status, 201)
    assert.deepStrictEqual(res.body, newUser)
    assert.ok(
      db.createUser.calledOnceWith({ name: "Bob", email: "bob@example.com" })
    )
  })

  it("POST /users - should return 400 if missing fields", async () => {
    const res = await request(app)
      .post("/users")
      .set("Authorization", `Bearer ${TOKEN}`)
      .send({ name: "Bob" })

    assert.strictEqual(res.status, 400)
    assert.deepStrictEqual(res.body, { error: "Missing name or email" })
  })

  it("POST /users - should return 401 if token is invalid", async () => {
    const res = await request(app)
      .post("/users")
      .set("Authorization", "Bearer wrong-token")
      .send({ name: "Bob", email: "bob@example.com" })

    assert.strictEqual(res.status, 401)
    assert.deepStrictEqual(res.body, { error: "Unauthorized" })
  })
})
