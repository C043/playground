// import { JSDOM } from "jsdom"
// import ejs from "ejs"
// import { dirname } from "path"
// import path from "path"
// import { fileURLToPath } from "url"
// import assert from "assert"
// import { beforeEach, describe, it } from "mocha"
// import sinon from "sinon"
// import { fetch, Response } from "undici"
//
// const __filename = fileURLToPath(import.meta.url)
// const __dirname = dirname(__filename)
//
// // Here we define the ejs to test
// const targetFile = path.resolve(__dirname, "../views/homePage.ejs")
//
// ejs.renderFile(
//   targetFile,
//   {
//     jsGlobals: {
//       user: {
//         isAdmin: false
//       }
//     }
//   },
//   function (err, str) {
//     if (str) {
//       describe("Home Page", () => {
//         let dom
//         let body
//         let fetchStub
//
//         // Here we define a new dom before each test
//         beforeEach(() => {
//           dom = new JSDOM(str, {
//             runScripts: "dangerously",
//             resources: "usable"
//           })
//           body = dom.window.document.body
//
//           // Here we define the fetch as the undici simulated one
//           dom.window.fetch = fetch
//
//           // Here we spy on the fetch and we make it resolve
//           // to an empty object because we're not really going
//           // to make an http request, we're just testing the
//           // frontend, so we're making sure that the fetch has
//           // the right headers and body
//           fetchStub = sinon
//             .stub(dom.window, "fetch")
//             .resolves(new Response("{}"))
//         })
//         it("Fetch Button should be present and call fetch with correct URL, headers, and body on button click", async () => {
//           const button = body.querySelector("#post-button")
//
//           assert.ok(button, "Expected button to exist")
//
//           // Here we simulate a click on the button that triggers the fetch
//           button.dispatchEvent(
//             new dom.window.MouseEvent("click", { bubbles: true })
//           )
//
//           // This is important to be sure that the event is handled before we assert that the fetch has been triggered
//           await new Promise(r => setTimeout(r, 0))
//
//           sinon.assert.calledOnce(fetchStub)
//           sinon.assert.calledWith(
//             fetchStub,
//             "/api/trigger-action",
//             sinon.match({
//               method: "POST",
//               headers: { Authorization: "Bearer token" },
//               body: JSON.stringify({
//                 name: "Mario",
//                 email: "example@gmail.com"
//               })
//             })
//           )
//         })
//       })
//     } else {
//       throw new Error("EJS NOT RENDERED")
//     }
//   }
// )
