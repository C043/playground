// import { JSDOM } from "jsdom"
// import fs from "fs"
// import ejs from "ejs"
// import { dirname } from "path"
// import path from "path"
// import { fileURLToPath } from "url"
// import assert from "assert"
// import { beforeEach, describe, it } from "mocha"
//
// const __filename = fileURLToPath(import.meta.url)
// const __dirname = dirname(__filename)
//
// const targetFile = path.resolve(__dirname, "../views/listPage.ejs")
//
// // Test data used both for rendering and for the client script
// const testBlogs = [
//   { title: "blog1", tag: "ai" },
//   { title: "blog2", tag: "ai" },
//   { title: "blog3", tag: "testing" }
// ]
//
// ejs.renderFile(targetFile, { blogList: testBlogs }, function (err, str) {
//   if (err) throw err
//   if (!str) throw new Error("EJS NOT RENDERED")
//
//   // Remove external script tag to avoid jsdom trying to fetch it
//   const sanitized = str.replace('<script src="/js/listPage.js"></script>', "")
//
//   describe("List Page", () => {
//     let dom
//     let body
//
//     beforeEach(() => {
//       dom = new JSDOM(sanitized, {
//         runScripts: "dangerously",
//         url: "http://localhost"
//       })
//       body = dom.window.document.body
//
//       // Provide the global the page script expects and load it manually
//       dom.window.blogList = testBlogs
//       const scriptPath = path.resolve("./public/js/listPage.js")
//       const scriptContent = fs.readFileSync(scriptPath, "utf8")
//       dom.window.eval(scriptContent)
//     })
//
//     it("renders all blogs initially", () => {
//       assert.equal(body.querySelectorAll(".blog-card").length, 3)
//     })
//
//     it("filters blogs by AI tag when button clicked", () => {
//       const btn = dom.window.document.querySelector("#filter-btn-ai")
//       btn.dispatchEvent(new dom.window.MouseEvent("click", { bubbles: true }))
//       assert.equal(dom.window.document.querySelectorAll(".blog-card").length, 2)
//     })
//   })
// })
