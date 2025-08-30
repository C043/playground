// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const occurrences = nums.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1
    return acc
  }, {})

  const filtered = Object.fromEntries(
    Object.entries(occurrences).filter(([key, value]) => value === 1)
  )

  const array = Object.keys(filtered)

  return array[0]
}
// @leet end
//
