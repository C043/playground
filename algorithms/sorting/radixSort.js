const getDigit = (num, place) => {
  const digits = num.toString().split("").reverse();
  const digit = parseInt(digits[place]);
  if (digit / digit !== 1) return 0;
  else return digit;
};

const digitCount = (num) => {
  return num.toString().length;
};

const mostDigits = (arr) => {
  let maxDigits = 0;
  arr.forEach((num) => (maxDigits = Math.max(maxDigits, digitCount(num))));
  return maxDigits;
};

const radixSort = (nums) => {
  const maxDigit = mostDigits(nums);
  for (let i = 0; i <= maxDigit; i++) {
    const digitBuckets = Array.from({ length: 10 }, () => []);
    nums.forEach((num) => {
      digitBuckets[getDigit(num, i)].push(num);
    });
    nums = [].concat(...digitBuckets);
  }
  return nums;
};

console.log(radixSort([501, 500, 4892, 1, 123456, 87, 642, 1, 89]));
