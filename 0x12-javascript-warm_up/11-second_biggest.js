#!/usr/bin/node
let args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  let mySet = new Set();
  for (let i = 2; i < args.length; i++) {
    mySet.add(args[i]);
  }
  let ArrayOfInts = Array.from(mySet).map(str => parseInt(str));
  let SortedArray = ArrayOfInts.sort((a, b) => a - b);
  let index = SortedArray.length - 2;
  console.log(SortedArray[index]);
}
