#!/usr/bin/node

const filesystem = require('fs');
const file1 = filesystem.readFileSync(process.argv[2], 'utf-8');
const file2 = filesystem.readFileSync(process.argv[3], 'utf-8');
filesystem.writeFileSync(process.argv[4], file1 + file2);
