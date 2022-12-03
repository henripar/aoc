let fs = require('fs');
const input = fs.readFileSync('./input.txt', 'utf-8').toString();

const backpackItemsList = input.split('\n');

function findCommonCharacters(s1, s2, s3) {
  for (let i in s1) {
    let commonChar = s2.includes(s1[i]) && s3.includes(s1[i]) ? s1[i] : false;
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

const findSumOfAuthenticationBadges = (input) => {
  counter = 0;
  points = 0;
  let group = [];
  for (const backpack of input) {
    group.push(backpack);

    if (group.length == 3) {
      let common = findCommonCharacters(group[0], group[1], group[2]);
      let pointsToAdd = countPoints(common);
      points += pointsToAdd;
      console.log(points);
      group = [];
    }
  }
  console.log(points);
};

findSumOfAuthenticationBadges(backpackItemsList);
