// @leet start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let result = 1

  // Three ways you can climb in total:
  // 1. One step at a time (This can always be done)
  // 2. Two steps (This can always be done if n % 2 === 0)
  if (n % 2 === 0) result++

  // 3. One step and Two steps
  // 4. Two steps and One step
  // The last ones can be done if one of them can be done
  if (n % 2 != 0 && n > 1) result = result + 2

  return result
}
// @leet end

console.log(climbStairs(45))
