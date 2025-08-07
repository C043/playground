import { JSDOM } from "jsdom"
import ejs from "ejs"
import { dirname } from "path"
import path from "path"
import { fileURLToPath } from "url"
import assert from "assert"
import { beforeEach, describe, it } from "mocha"
import sinon from "sinon"
import { fetch, Response } from "undici"

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const targetFile = path.resolve(__dirname, "../views/homePage.ejs")

ejs.renderFile(targetFile, function (err, str) {
  if (str) {
    describe("Home Page", () => {
      let dom
      let body
      let fetchStub

      beforeEach(() => {
        dom = new JSDOM(str, { runScripts: "dangerously", resources: "usable" })
        body = dom.window.document.body

        dom.window.fetch = fetch

        fetchStub = sinon.stub(dom.window, "fetch").resolves(new Response("{}"))
      })

      it("h1 should be present and have specific text", () => {
        assert.equal(body.querySelector("h1").textContent, "Home Page")
      })

      it("Button should be present and call fetch with correct URL on button click", async () => {
        const button = body.querySelector("#post-button")

        assert.ok(button, "Expected button to exist")

        button.dispatchEvent(
          new dom.window.MouseEvent("click", { bubbles: true })
        )

        await new Promise(r => setTimeout(r, 0))

        sinon.assert.calledOnce(fetchStub)
        sinon.assert.calledWith(
          fetchStub,
          "/api/trigger-action",
          sinon.match.has("method", "POST")
        )
      })
    })
  }
})
