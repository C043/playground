import assert from "assert"
import { chromium } from "playwright"
import http from "http"
import app from "../app.js"

let server, serverUrl, browser, page

describe("Dialog behavior", function () {
  before(async () => {
    await new Promise(r => {
      server = http.createServer(app)
      server.listen(0, () => {
        const { port } = server.address()
        serverUrl = `http://localhost:${port}`
        r()
      })
    })

    browser = await chromium.launch({ headless: true })
    page = await browser.newPage()
  })

  after(async () => {
    await browser.close()
    await new Promise(r => server.close(r))
  })

  it("should show modal when open button is clicked", async () => {
    await page.goto(serverUrl)
    const dialog = page.locator("#dialog")

    await page.click("#open-dialog")

    const hasOpen = await dialog.evaluate(el => el.hasAttribute("open"))

    assert.strictEqual(hasOpen, true)
  })
})
