export function renderHomePage(req, res) {
  return res.render("homePage", {
    jsGlobals: {
      user: {
        isAdmin: false
      }
    },
    title: "EJS TESTING"
  })
}
