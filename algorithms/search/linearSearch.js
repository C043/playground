const linearSearch = (arr, val) => {
  if (arr.length === 0) return -1;
  for (let i = 0; i < arr.length; i++) {
    const currentVal = arr[i];
    if (currentVal === val) return i;
  }
  return -1;
};

console.log(linearSearch([1, 2, 3, 4, 5, 6, 60], -1));

const linearRecursion = (arr, val) => {
  if (arr.length === 0) return false;
  if (arr[0] === val) return true;
  return linearRecursion(arr.slice(1), val);
};

console.log(linearRecursion([1, 2, 3, 4, 5, 6, 7, 60], -1));
