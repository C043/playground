const collectOddValues = (arr) => {
  let newArr = [];

  function helper(recursiveArr) {
    if (recursiveArr.length === 0) return;

    if (recursiveArr[0] % 2 !== 0) newArr.push(recursiveArr[0]);

    helper(recursiveArr.slice(1));
  }

  helper(arr);

  return newArr;
};

const collectOddValuesPureRecursive = (arr) => {
  let newArr = [];
  // Base Case
  if (arr.length === 0) return newArr;

  // Recursive Case
  if (arr[0] % 2 !== 0) newArr.push(arr[0]);
  return newArr.concat(collectOddValuesPureRecursive(arr.slice(1)));
};

console.log(collectOddValues([1, 2, 3, 4]));

console.log(collectOddValuesPureRecursive([1, 2, 3, 4]));
