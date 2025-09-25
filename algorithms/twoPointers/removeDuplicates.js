const removeDuplicates = (arr) => {
  // Se l'array è vuoto o ha un solo elemento lo ritorno
  if (arr.length === 0 || arr.length === 1) return arr;
  // Inizializzo i due puntatori partendo dall'inizio
  let i = 0;
  let j = 1;
  // ciclo l'array tenendo conto dell'ultimo elemento unico trovato
  while (j <= arr.length - 1) {
    if (arr[i] === arr[j]) {
      j++;
    } else {
      i++;
      arr.splice(i, 1, arr[j]);
    }
  }
  // ritorno l'array senza duplicati
  return arr.slice(0, i + 1);
};

console.log(removeDuplicates([]));
console.log(
  removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 20]),
);
