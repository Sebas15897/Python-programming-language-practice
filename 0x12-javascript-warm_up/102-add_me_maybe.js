#!/usr/bin/nodejs
function addMeMaybe (number, thefunction) {
  number += 1;
  thefunction(number);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
