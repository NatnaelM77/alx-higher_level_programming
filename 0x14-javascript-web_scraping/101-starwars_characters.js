#!/usr/bin/node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (err, res, body) {
  if (err) throw err;

  const data = JSON.parse(body);

  data.characters.forEach(function (url, index){
    request.get(url, function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  });
});
