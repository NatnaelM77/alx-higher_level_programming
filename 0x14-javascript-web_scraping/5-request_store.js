#!/usr/bin/node

const { spawn } = require('child_process');
const request = require('request');

request.get(process.argv[2], function (err, res, body) {
  if (err) throw err;
  spawn('./1-writeme.js', [process.argv[3], body]);
});
