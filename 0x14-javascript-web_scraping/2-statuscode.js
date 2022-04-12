#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res) {
  if (err) throw err;
  console.log(`code: ${res && res.statusCode}`);
});
