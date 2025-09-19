// @leet start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  const results = {}

  function recursiveClimb(n) {
    if (n <= 1) return 1
    let oneStep = null
    let twoSteps = null
    if (results[n - 1]) {
      oneStep = results[n - 1]
    } else {
      results[n - 1] = recursiveClimb(n - 1)
      oneStep = results[n - 1]
    }
    if (results[n - 2]) {
      twoSteps = results[n - 2]
    } else {
      results[n - 2] = recursiveClimb(n - 2)
      twoSteps = results[n - 2]
    }
    if (n > 1) return oneStep + twoSteps
  }

  return recursiveClimb(n)
}
// @leet end
console.log(climbStairs(44))
