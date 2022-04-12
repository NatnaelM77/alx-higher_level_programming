#!/usr/bin/node

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/people/18', function (err, res, body) {
  if (err) throw err;
  console.log(JSON.parse(body).films.length);
});
