import express from "express"
import { createUserRouter } from "./routes/user.js"

export function createApp(db, requiredToken) {
  const app = express()
  app.use(express.json())
  app.use("/users", createUserRouter(db, requiredToken))
  return app
}
