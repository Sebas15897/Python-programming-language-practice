#!/usr/bin/node
const number = process.argv[2];

if (isNaN(number)) console.log('Missing size');
else {
  for (let i = 0; i < number; i++) {
    let msg = '';
    for (let j = 0; j < number; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}
