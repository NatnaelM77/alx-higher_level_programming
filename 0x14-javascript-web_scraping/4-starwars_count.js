#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res, body) {
  let count = 0;
  const data = JSON.parse(body);
  const reg = /18/g;

  if (err) throw err;

  for (let i = 0; i < data.results.length; i++) {
    for (let j = 0; j < data.results[i].characters.length; j++) {
      if (reg.test(data.results[i].characters[j])) {
        count += 1;
      }
    }
  }

  console.log(count);
});
