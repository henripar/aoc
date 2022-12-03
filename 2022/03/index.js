let fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8').toString();

const backpackItemsList = input.split('\n');

function splitStrinFromHalf(str, index) {
  const result = [str.slice(0, index), str.slice(index)];

  return result;
}

function findCommonCharacters(s1, s2) {
  var commonCharacter = '';

  for (let i in s1) {
    let commonChar = s2.includes(s1[i]) ? s1[i] : false;
    if (commonChar != '') {
      return commonChar;
    }
  }
}

let countPoints = (letter) => {
  const alpha = Array.from(Array(26)).map((e, i) => i + 65);
  const alphabetCapital = alpha.map((x) => String.fromCharCode(x));

  const alphabetLowercase = alphabetCapital.map((a) => a.toLocaleLowerCase());
  if (alphabetCapital.includes(letter)) {
    const points = alphabetCapital.indexOf(letter, 0) + 27;
    console.log('Point = ' + points);
    return points;
  }
  if (alphabetLowercase.includes(letter)) {
    const points = alphabetLowercase.indexOf(letter, 0) + 1;
    console.log('point = ' + points);
    return points;
  }
};

// console.log(playsArray);

let allPoints = 0;

for (const backpack of backpackItemsList) {
  console.log(backpack.length);
  let middle = Math.floor(backpack.length / 2);
  let [firstCompartment, secondCompartment] = splitStrinFromHalf(
    backpack,
    middle
  );
  console.log(firstCompartment, secondCompartment);

  let cc = findCommonCharacters(firstCompartment, secondCompartment);

  let points = countPoints(cc);
  if (points > 0) {
    allPoints = allPoints + points;
  }
}

console.log(allPoints);
