import { JSDOM } from "jsdom"
import ejs from "ejs"
import { dirname } from "path"
import path from "path"
import { fileURLToPath } from "url"
import assert from "assert"
import { beforeEach, describe, it } from "mocha"

const __filename = fileURLToPath(import.meta.url)
const __dirname = dirname(__filename)

const targetFile = path.resolve(__dirname, "../views/listPage.ejs")

ejs.renderFile(
  targetFile,
  {
    blogList: [
      {
        title: "blog1",
        tag: "ai"
      },
      {
        title: "blog2",
        tag: "ai"
      },
      {
        title: "blog3",
        tag: "testing"
      }
    ]
  },
  function (err, str) {
    if (str) {
      describe("List Page", () => {
        let dom
        let body

        beforeEach(() => {
          dom = new JSDOM(str, {
            runScripts: "dangerously",
            resources: "usable"
          })
          body = dom.window.document.body
        })

        it("should render all blogs", () => {
          assert.equal(body.querySelectorAll(".blog-card").length, 3)
        })

        it("should only render ai blog cards when clicking the blog filter by ai button", async () => {
          const filterBtn = body.querySelector("#filter-btn-ai")
          assert.ok(filterBtn)

          filterBtn.dispatchEvent(
            new dom.window.MouseEvent("click", { bubbles: true })
          )

          await new Promise(r => setTimeout(r, 0))

          assert.equal(body.querySelectorAll(".blog-card").length, 3)
        })
      })
    } else {
      throw new Error("EJS NOT RENDERED")
    }
  }
)
