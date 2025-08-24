// @leet start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false

  const digits = x.toString().split("")

  for (let i = 1; i < digits.length; i++) {
    if (digits[i - 1] !== digits[digits.length - i]) return false
  }

  return true
}
// @leet end
const test = isPalindrome(121)
console.log(test)
