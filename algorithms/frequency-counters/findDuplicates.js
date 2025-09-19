const findDuplicates = (arr) => {
  // Inizializzo il frequency counter
  const frequencyCounter = {};
  // Inizializzo un array result
  const result = [];
  // Ciclo l'array e tengo traccia della frequenza degli elementi
  arr.forEach((value) => {
    frequencyCounter[value]
      ? (frequencyCounter[value] += 1)
      : (frequencyCounter[value] = 1);
  });
  // Ciclo l'oggetto e pusho tutti gli elementi che hanno valore più di uno
  // nell'array result
  const keys = Object.keys(frequencyCounter);
  const values = Object.values(frequencyCounter);
  values.forEach((value, index) => {
    if (value > 1) result.push(keys[index]);
  });
  // ritorno l'array result
  return result;
};

console.log(findDuplicates([1, 1, 2, 3, 3, 4, 56, 6, 6]));
