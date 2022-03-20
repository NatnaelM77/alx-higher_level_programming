#!/usr/bin/node

const list = require('./100-data.js').list;

function newArray (array) {
  const newArray = array.map((index, value) => index * value);
  return newArray;
}

console.log(list);
console.log(newArray(list));
