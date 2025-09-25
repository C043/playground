const swap = (arr, idx1, idx2) => {
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]
}

const selectionSort = arr => {
  for (let i = 0; i < arr.length; i++) {
    let noSwap = true
    let min = i
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) min = j
    }
    if (i !== min) {
      swap(arr, i, min)
      noSwap = false
    }
    if (noSwap) break
  }
  return arr
}

console.log(selectionSort([5, 2, 7, 1, 9, 10]))
console.log(selectionSort([5, 1, 6, 3, 8, 2, 9, 1, 1]))
