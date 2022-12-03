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
  let oneMatch = 0;
  for (let char = 1; char <= passwordLength + 1; char++) {
    let character = pw[char - 1];
    let position1 = passsword[0].split('-')[0];
    let position2 = passsword[0].split('-')[1];

    console.log(position2);

    if (char == position1 && character == passsword[1][0]) {
      oneMatch++;
    }

    if (char == position2 && character == passsword[1][0]) {
      oneMatch++;
    }
    if (char == passwordLength + 1) {
      oneMatch == 1 ? goodPassWordsCount++ : null;
    }
  }
}

console.log(goodPassWordsCount);
console.log(inputArray.length);
