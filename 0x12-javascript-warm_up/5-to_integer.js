#!/usr/bin/node
const stringToNumber = parseInt(process.argv[2]);
if (isNaN(stringToNumber)) console.log('Not a number');
else console.log(`My number: ${stringToNumber}`);
