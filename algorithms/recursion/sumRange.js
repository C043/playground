const sumRange = (num) => {
  // Base Case
  if (num === 1) return 1;
  // Recursive Case
  return num + sumRange(num - 1);
};

console.log(sumRange(3));
console.log(sumRange(4));
