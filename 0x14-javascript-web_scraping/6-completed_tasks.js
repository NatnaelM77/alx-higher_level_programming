#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  let tmp = '';
  const obj = {};
  if (err) throw err;

  const data = JSON.parse(body);
  for (let i = 0; i < data.length; i++) {
    tmp = data[i].userId;
    if (data[i].completed) {
      obj[data[i].userId] = (obj[tmp] || 0) + 1;
    }
  }
  console.log(obj);
});
