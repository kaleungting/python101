function removeVowels(str) {
  let vowels = new Set(["a", "e", "i", "o", "u"]);
  let newStr = "";

  for (let char of str) {
    if (!vowels.has(char.toLowerCase())) {
      newStr += char;
    }
  }

  return newStr;
}

console.log(removeVowels("hello"));
