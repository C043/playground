// @leet start
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  if (digits.length === 0) return [1]

  let lastDigit = digits[digits.length - 1]
  if (lastDigit >= 9) {
    lastDigit = 0
    return plusOne(digits.slice(0, digits.length - 1)).concat(lastDigit)
  } else {
    digits[digits.length - 1] = lastDigit + 1
  }
  return digits
}
// @leet end

console.log(plusOne([9, 9, 9]))
