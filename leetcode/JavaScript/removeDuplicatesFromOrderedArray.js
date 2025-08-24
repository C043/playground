// @leet start
/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  if (nums.length === 0) return 0

  let writeIdx = 0
  for (let i = 1; i < nums.length; i++) {
    const firstPointer = nums[writeIdx]
    const secondPointer = nums[i]

    if (firstPointer !== secondPointer) {
      writeIdx++
      nums[writeIdx] = secondPointer
    }
  }

  return nums.slice(0, writeIdx + 1).length
}
// @leet end
