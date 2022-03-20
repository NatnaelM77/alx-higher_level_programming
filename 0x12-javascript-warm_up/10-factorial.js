#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

if (process.argv.length > 2) {
  console.log(factorial(process.argv[2]));
} else {
  console.log(1);
}
