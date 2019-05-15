#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let results;
let count = 0;
let i;
let c;
let characters;
let NumberResults;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).results;
    NumberResults = results.length;
    for (i = 0; i < NumberResults; i++) {
      characters = results[i].characters;
      for (c = 0; c < characters.length; c++) {
        if (characters[c].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
