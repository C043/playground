import express from "express"
const router = express.Router()
import * as controller from "../controllers/controller.js"

router.get("/", (req, res) => {
  controller.renderHomePage(req, res)
})

router.get("/listPage", (req, res) => {
  controller.renderListPage(req, res)
})

export default router
