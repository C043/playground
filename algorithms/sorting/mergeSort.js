const merge = (arr1, arr2) => {
  let newArr = [];
  let i = 0;
  let j = 0;
  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      newArr.push(arr1[i]);
      i++;
    } else {
      newArr.push(arr2[j]);
      j++;
    }
  }
  if (i !== arr1.length) newArr = newArr.concat(arr1.slice(i));
  if (j !== arr2.length) newArr = newArr.concat(arr2.slice(j));
  return newArr;
};

// console.log(merge([0, 1, 2, 5, 7, 10], [-5, 0, 1, 2]));

const mergeSort = (arr) => {
  // Base Case
  if (arr.length <= 1) return arr;
  // Recursive Case
  const splittedArr1 = arr.slice(0, Math.floor(arr.length / 2));
  const splittedArr2 = arr.slice(Math.floor(arr.length / 2));
  return merge(mergeSort(splittedArr1), mergeSort(splittedArr2));
};

console.log(mergeSort([5, -2, 6, -5, 34, 1, 5]));
