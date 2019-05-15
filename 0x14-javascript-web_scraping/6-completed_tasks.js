#!/usr/bin/node
// script that computes the number of tasks completed by id
const request = require('request');
let url = process.argv[2];
let index;
let results;
request(url, function (error, response, body) {
	results = JSON.parse(body)
	console.log(typeof(results))
	if (error) {
		console.log(error);
	} else {
		//#for (index = 0; index < results.length; index++) {
		//	# for each task check id and if task has been completed.
		//	# if true than add it to a value.dic[user] = val
		a = 1
		console.log(results[8])
		console.log(a)
		console.log(results[8]['userId'])
		console.log(results[8]['completed'])
		userId = results[8]['userId']
		console.log("userId: " + userId)
		let users = {}
		if (results[8]['completed'] === true) {
			console.log("Huuray" + results[8]['userId'] + " has finished the task")
			if (users[userId] === undefined) {
				users[userId] = 0;
			}
			users[userId] += 1;

		}


		console.log(users)
		}
});
