import express from "express"
const router = express.Router()
import * as controller from "../controllers/controller.js"

router.get("/", (req, res) => {
  controller.renderHomePage(req, res)
})

export default router
