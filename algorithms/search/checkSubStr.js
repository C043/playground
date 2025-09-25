// Naive Solution
const checkSubStr = (str, subStr) => {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    for (let j = 0; j < subStr.length; j++) {
      const currentChar = str[i + j];
      const currentSubChar = subStr[j];
      if (currentChar !== currentSubChar) break;
      else if (j === subStr.length - 1) count++;
    }
  }
  return count;
};

console.log(checkSubStr("abcaabcdbbabcd", "abc"));
