const swap = (arr, idx1, idx2) => {
  console.log("SWAP!");
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
};

const bubbleSort = (arr) => {
  for (let i = arr.length; i >= 0; i--) {
    let noSwap = true
    for (let j = 0; j < i - 1; j++) {
      console.log(arr, arr[j], arr[j + 1]);
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
        noSwap = false
      }
    }
    if (noSwap) break
  }
  return arr;
};

console.log(bubbleSort([1, 2, 3, 4, 5, 50, 6]))
//console.log(bubbleSort([5, 10, 6, 8, 9, 2, 0]));
//console.log(bubbleSort([20, 56, 48, 1, 0, 1010]));
