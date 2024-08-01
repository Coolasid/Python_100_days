// guess.js

const LOW = 1;
const HIGH = 10;

let secretNumber = Math.floor(Math.random() * HIGH) + LOW;
let clue = '';
let number = null;

do {
  const readlineSync = require('readline-sync');
  let guess = readlineSync.question(
    `Guess a number between ${LOW} and ${HIGH} ${clue}`
  );
  number = parseInt(guess);
  if (number > secretNumber) {
    clue = `(less than ${number})`;
  } else if (number < secretNumber) {
    clue = `(greater than ${number})`;
  }
} while (number != secretNumber);

alert(`You guessed it! The secret number is ${number}`);
