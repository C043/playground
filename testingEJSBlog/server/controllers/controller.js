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

export function renderListPage(req, res) {
  return res.render("listPage", {
    title: "EJS LIST TESTING",
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
  })
}
