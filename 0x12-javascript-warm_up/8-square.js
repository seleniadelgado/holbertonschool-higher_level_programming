#!/usr/bin/node
let args = process.argv;

let X = parseInt(args[2]);
let i;
if (isNaN(X)) {
  console.log('Missing size');
} else {
  for (i = 0; i < X; i++) { console.log('X'.repeat(X)); }
}
