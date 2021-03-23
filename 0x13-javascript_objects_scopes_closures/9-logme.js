#!/usr/bin/node
// function that prints the number of arguments already printed and the new argument value.
let total = 0;
exports.logMe = item => {
  console.log(total + ': ' + item);
  total += 1;
};
