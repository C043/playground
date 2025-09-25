const blogList = window.blogList
function filterBlogsByAI() {
  const filtered = blogList.filter(blog => blog.tag === "ai")
  const blogsContainer = document.getElementById("blogs-container")
  blogsContainer.innerHTML = ""

  filtered.forEach(blog => {
    const blogCard = document.createElement("div")
    blogCard.classList.add("blog-card")

    const title = document.createElement("h1")
    title.innerText = blog.title

    const blogTag = document.createElement("p")
    blogTag.innerText = blog.tag

    blogCard.appendChild(title)
    blogCard.appendChild(blogTag)

    blogsContainer.appendChild(blogCard)
  })
}
