#!/usr/bin/node
// script that matches episode number to a given integer
// get episode number
// request API with the correct endpoint
const request = require('request');
let url = 'http://swapi.co/api/films/';
let episode = process.argv[2];
let path = url + episode;
request(path, function (error, response, body) {
  if (error) {
    console.log(error);
  } else { console.log(JSON.parse(body).title); }
}
);
