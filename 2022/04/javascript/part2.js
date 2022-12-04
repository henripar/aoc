let fs = require('fs');
const input = fs.readFileSync('../input.txt', 'utf-8').toString();

let assignmentPairs = input.split('\n');

console.log(assignmentPairs);

assignmentPairs = assignmentPairs.map((assignmentPair) =>
  assignmentPair.split(',')
);

let partialMatchesAmount = 0;

for (const assignmentPair of assignmentPairs) {
  let assignment1start = +assignmentPair[0].split('-')[0];
  let assignment1end = +assignmentPair[0].split('-')[1];

  let assignment2start = +assignmentPair[1].split('-')[0];
  let assignment2end = +assignmentPair[1].split('-')[1];

  // Check if first range is fully before the second

  if (
    assignment1start < assignment2start &&
    assignment1end < assignment2start
  ) {
    console.log('no overlap');
  }

  // Check if second range is fully before the first
  else if (
    assignment2start < assignment1start &&
    assignment2end < assignment1start
  ) {
    console.log('no overlap');
  } else {
    partialMatchesAmount += 1;
  }
}

console.log(partialMatchesAmount);
