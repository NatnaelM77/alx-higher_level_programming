#!/usr/bin/node

if (process.argv.length > 3) {
  const arr = process.argv.slice(2).map(Number);

  arr.splice(arr.indexOf(Math.max.apply(null, arr)), 1);
  console.log(Math.max.apply(null, arr));
} else {
  console.log(0);
}
