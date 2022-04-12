#!/usr/bin/node

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/people/18', function (err, res, body){
	console.log(JSON.parse(body).films.length)
});
