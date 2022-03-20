#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length;
  const reverseArray = [];
  while (--i > -1) {
    reverseArray.push(list[i]);
  }
  return (reverseArray);
};
