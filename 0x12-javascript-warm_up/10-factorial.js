#!/usr/bin/node
function factorial (n) {
  let a = parseInt(n, 10);
  if (a === 1 || isNaN(a)) {
    return 1;
  } else {
    return (factorial(a - 1) * a);
  }
}
let args = process.argv;
let n = args[2];
console.log(factorial(n));
