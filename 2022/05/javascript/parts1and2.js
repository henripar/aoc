let fs = require('fs');

let [inputStacks, inputInstructions] = fs
  .readFileSync('../input.txt', 'utf8')
  .toString()
  .trim()
  .split('\n\n');

let inputStacksLines = inputStacks.split('\n');

// Remove stack numbers line

inputStacksLines.pop();

const stacks = [];

for (let inputStacLine of inputStacksLines) {
  for (let i = 0; i < inputStacLine.length; i += 3 + 1) {
    let start = i;
    let end = start + 3;
    let crate = inputStacLine.substring(start, end);

    let stackIndex = i / (3 + 1);
    if (!stacks[stackIndex]) {
      stacks[stackIndex] = [];
    }
    if (crate.trim()) {
      stacks[stackIndex].push(crate.substring(1, 2));
    }
  }
}

for (let stack of stacks) {
  stack.reverse();
}

let instructions = inputInstructions.split('\n').map((line) => {
  let instruction = line.split(' ');
  let amount = parseInt(instruction[1], 10);
  let source = parseInt(instruction[3], 10) - 1;
  let destination = parseInt(instruction[5], 10) - 1;

  return { amount, source, destination };
});

const partOne = () => {
  let stacksForPart1 = JSON.parse(JSON.stringify(stacks));
  for (let { amount, source, destination } of instructions) {
    for (let c = 0; c < amount; c++) {
      let crate = stacksForPart1[source].pop();
      stacksForPart1[destination].push(crate);
    }
  }

  return stacksForPart1.map((stack) => stack[stack.length - 1]).join('');
};

const partTwo = () => {
  let stacksForPart2 = JSON.parse(JSON.stringify(stacks));
  for (let { amount, source, destination } of instructions) {
    let cratesStack = stacksForPart2[source].splice(-1 * amount, amount);
    stacksForPart2[destination].push(...cratesStack);
  }

  return stacksForPart2.map((stack) => stack[stack.length - 1]).join('');
};

let topCratesPart1 = partOne();

let topCratesPart2 = partTwo();

console.log('Part one top crates:', topCratesPart1);
console.log('Part two top crates:', topCratesPart2);
