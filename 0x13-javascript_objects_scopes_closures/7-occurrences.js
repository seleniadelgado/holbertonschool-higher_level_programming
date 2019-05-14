#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
// iterate through list
  let i;
  let counter = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
