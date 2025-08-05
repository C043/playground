import { Router } from "express"

export function createUserRouter(db, requiredToken) {
  const router = Router()

  const authenticate = (req, res, next) => {
    const authHeader = req.headers["authorization"] || ""
    const token = authHeader.replace("Bearer ", "")

    if (token !== requiredToken) {
      return res.status(401).json({ error: "Unauthorized" })
    }

    next()
  }

  router.get("/:id", authenticate, async (req, res) => {
    const user = await db.getUserById(req.params.id)
    if (!user) return res.status(404).json({ error: "User not found" })
    res.json(user)
  })

  router.post("/", authenticate, async (req, res) => {
    const { name, email } = req.body
    if (!name || !email) {
      return res.status(400).json({ error: "Missing name or email" })
    }

    const newUser = await db.createUser({ name, email })
    res.status(201).json(newUser)
  })

  return router
}
