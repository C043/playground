const checkUniqueValues = (arr, value) => {
  // Inizializzo il frequency counter obj
  const frequencyCounter = {};
  // Ciclo l'array tenendo traccia delle frequenze
  arr.forEach((value) => {
    frequencyCounter[value]
      ? (frequencyCounter[value] += 1)
      : (frequencyCounter[value] = 1);
  });
  // ciclo l'oggetto tenendo traccia di quanti valori 1 ci sono
  const values = Object.values(frequencyCounter);
  let counter = 0;
  values.forEach((value) => value === 1 && counter++);
  // Ritorno true se vi sono abbastanza uno e false se no
  return counter >= value;
};

const array = [1, 2, 3, 3, 3, 3, 3, 3];
const value = 3;
console.log(checkUniqueValues(array, value));
