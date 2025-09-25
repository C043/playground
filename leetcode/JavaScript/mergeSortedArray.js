// @leet end
// @leet start
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  for (let i = 1; i <= n; i++) {
    nums1.pop()
  }

  nums1.push(...nums2)
  nums1.sort((a, b) => a - b)
}
// @leet end

const nums1 = [-10, 2, 0]
const nums2 = [-1, 1]
merge(nums1, nums1.length - nums2.length, nums2, nums2.length)
console.log(nums1)
