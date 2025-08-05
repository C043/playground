export function auth(requiredToken) {
  return (req, res, next) => {
    const authHeader = req.headers["authorization"] || ""
    const token = authHeader.replace("Bearer ", "")

    if (token !== requiredToken) {
      return res.status(401).json({ error: "Unauthorized" })
    }

    next()
  }
}
