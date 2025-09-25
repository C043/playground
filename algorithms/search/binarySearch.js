const binarySearch = (arr, val) => {
  if (arr.length === 0) return -1;

  let min = 0;
  let max = arr.length - 1;

  while (min <= max) {
    let middle = Math.floor((min + max) / 2);
    if (arr[middle] > val) max = middle - 1;
    else if (arr[middle] < val) min = middle + 1;
    else return middle;
  }
  return -1;
};

console.log(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 20], 204));
console.log(binarySearch([]));

const binaryRecursion = (arr, val) => {
  if (arr.length === 0) return false;

  let min = 0;
  let max = arr.length - 1;

  let middle = Math.floor((min + max) / 2);

  if (arr[middle] > val) return binaryRecursion(arr.slice(0, middle - 1), val);
  else if (arr[middle] < val)
    return binaryRecursion(arr.slice(middle + 1), val);
  else return true;
};

console.log(binaryRecursion([1, 2, 3, 4, 5, 6, 7, 9], 2));
console.log(binaryRecursion([1, 2, 3, 4, 5, 6, 7, 9], -3));
