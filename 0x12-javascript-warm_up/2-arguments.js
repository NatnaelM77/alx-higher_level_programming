#!/usr/bin/node

if (process.argv.length > 2) {
  if (process.argv.length === 3) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
} else {
  console.log('No argument');
}
