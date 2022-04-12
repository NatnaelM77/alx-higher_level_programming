#!/usr/bin/node

const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (err, res, body) {
  if (err) throw err;

  let data = JSON.parse(body);

  for (let url of data.characters)
  {
    request.get(url, function (err, res, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
