import { config as dotenvConfig } from "dotenv"
dotenvConfig()
import http from "http"
import express from "express"
import expressEjsLayouts from "express-ejs-layouts"

const app = express()

app.use(express.static("public"))
app.set("view engine", "ejs")
app.use(expressEjsLayouts)
app.set("layout", "layouts/main")

// ROUTES
import routes from "./server/routes/routes.js"

app.use("/", routes)

const httpServer = http.createServer(app)
const expressPort = process.env.HTTP_PORT

httpServer.timeout = 30000
httpServer.listen(expressPort, () => {
  console.log(`EXPRESS STARTED - Listening to http://localhost:${expressPort}`)
})
