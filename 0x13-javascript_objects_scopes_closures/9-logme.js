#!/usr/bin/node

exports.logMe = (function (item) {
  let number = 0;
  return function (item) {
    console.log(`${number++}: ${item}`);
  };
})();
