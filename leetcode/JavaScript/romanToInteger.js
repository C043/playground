// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const symbolValueMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000
  }

  const chars = s.split("")
  let result = 0

  for (let i = 0; i < chars.length; i++) {
    const currentNum = symbolValueMap[chars[i]]
    let num = currentNum
    const sequentNum = symbolValueMap[chars[i + 1]]
    console.log(currentNum)
    if (currentNum < sequentNum) {
      num = sequentNum - currentNum
      i = i + 1
    }
    result = result + num
  }

  return result
}
// @leet end

console.log(romanToInt("MCMXCIV"))
