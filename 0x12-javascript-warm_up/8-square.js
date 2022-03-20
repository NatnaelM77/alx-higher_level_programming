#!/usr/bin/node

const arg = process.argv[2];
let square = '';

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < arg; index++) {
    for (let index = 0; index < arg; index++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
}
