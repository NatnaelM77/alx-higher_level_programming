#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  if (err) throw err;
  const obj = {};
  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      obj[data[i].userId] = data[i].id;
    }
  }
  console.log(obj);
});
