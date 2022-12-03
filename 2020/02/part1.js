let fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8').toString();

inputArray = input.split('\n').map((value, index) => {
  return value.split(' ');
});
console.log(inputArray.length);
let goodPassWordsCount = 0;

for (let passsword of inputArray) {
  console.log(passsword);
  let passwordLength = passsword[2]?.length;
  console.log('PASSWORD', passsword[2]);
  let pw = passsword[2];
  let counter = 0;
  for (let char = 0; char <= passwordLength; char++) {
    let character = pw[char];

    if (character == passsword[1][0]) {
      counter++;
    }
  }
  if (
    counter >= passsword[0].split('-')[0] &&
    counter <= passsword[0].split('-')[1]
  ) {
    goodPassWordsCount += 1;
  }
}

console.log(goodPassWordsCount);
console.log(inputArray.length);
