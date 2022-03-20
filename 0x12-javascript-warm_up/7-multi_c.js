#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < arg; index++) {
    console.log('C is fun');
  }
}
