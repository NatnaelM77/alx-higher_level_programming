#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  let count = 0; let end = 20;
  const obj = {};
  if (err) throw err;

  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    if (data[i].completed === true) {
      count += 1;
      obj[data[i].userId] = count;
    }
    if (data[i].id === end) {
      count = 0;
      end += 20;
    }
  }
  console.log(obj);
});
