#!/usr/bin/node
// A script that displays a status code of a GET request
const request = require('request');
let URL = process.argv[2];
request
  .get(URL)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
