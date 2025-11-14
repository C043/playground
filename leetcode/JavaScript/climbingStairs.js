// @leet start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const results = {}

  function recursiveClimb(results, k) {
    if (k <= 1) return 1
    if (results[k]) {
      return results[k]
    }

    const result =
      recursiveClimb(results, k - 1) + recursiveClimb(results, k - 2)

    results[k] = result
    return result
  }

  return recursiveClimb(results, n)
}
// @leet end
console.log(climbStairs(44))
