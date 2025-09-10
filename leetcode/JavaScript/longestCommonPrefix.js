// @leet start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  if (strs.length === 0) return ""

  return strs.reduce((prefix, currentStr) => {
    let i = 0
    while (
      i < prefix.length &&
      i < currentStr.length &&
      prefix[i] === currentStr[i]
    ) {
      i++
    }

    return prefix.substring(0, i)
  })
}
// @leet end

console.log(longestCommonPrefix(["flower", "flower", "flower"]))
