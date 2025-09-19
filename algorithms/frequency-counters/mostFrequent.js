const mostFrequent = (arr) => {
  // Inizializzo un frequency counter
  const frequencyCounter = {};
  // Ciclo l'array e tengo traccia delle frequenze
  for (i in arr) {
    const value = arr[i];
    frequencyCounter[value]
      ? (frequencyCounter[value] += 1)
      : (frequencyCounter[value] = 1);
  }
  // Ciclo di nuovo l'array comparando gli elementi con le le loro frequenze e
  // tengo traccia della frequenza più alta
  let maxFrequency = 0;
  let result = 0;
  for (i in arr) {
    const value = arr[i];
    if (frequencyCounter[value] > maxFrequency) {
      result = value;
      maxFrequency = frequencyCounter[value];
    }
  }
  // Ritorno l'elemento con la frequenza più alta
  return result;
};

console.log(mostFrequent([1, 2, 1]));
console.log(mostFrequent([1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 8]));
