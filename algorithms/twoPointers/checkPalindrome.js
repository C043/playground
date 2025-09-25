const checkPalindrome = (str) => {
  if (str.length === 0) return false;
  // Inizializzo i puntatori
  let i = 0;
  let j = str.length - 1;
  // Controllo che i puntatori siano uguali
  while (j > i) {
    if (str[i] === str[j]) {
      i++;
      j--;
    } else return false;
  }
  // ritorno true o false
  return true;
};

console.log(checkPalindrome("itopinonavevanonipoti"));
console.log(checkPalindrome(""));
