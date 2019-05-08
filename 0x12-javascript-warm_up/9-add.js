#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}
let args = process.argv;
let a = args[2];
let b = args[3];
console.log(add(a, b));
