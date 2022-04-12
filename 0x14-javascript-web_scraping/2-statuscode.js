#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function(err, res){
	console.log(`code: ${res && res.statusCode}`);
});
