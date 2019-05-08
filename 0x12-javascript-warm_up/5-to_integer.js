#!/usr/bin/node

let args = process.argv;

let number = parseInt(args[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
