// @leet start
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  const filtered = nums.filter(num => num !== val)
  for (const [idx, num] of filtered.entries()) {
    nums[idx] = num
  }
  return filtered.length
}
// @leet end

const array = [3, 2, 2, 3]
console.log(removeElement(array, 3))
