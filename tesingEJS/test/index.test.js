import { JSDOM } from "jsdom"
import ejs from "ejs"
import path from "path"

const targetFile = path.resolve(__dirname, "../views/index.ejs")

ejs.renderFile(targetFile, function (err, str) {
  if (str) {
    let dom
    let container

    describe("Home Page", () => {
      dom = new JSDOM(str)
      container = dom.window.document.body
    })

    test("h1 should be present and have specific text", () => {
      console.log(container.querySelector("h1").textContent)
    })
  }
})
