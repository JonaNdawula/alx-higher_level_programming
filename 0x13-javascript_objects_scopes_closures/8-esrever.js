#!/usr/bin/node

exports.esrever = function (list) {
  const ls = [];
  let x = 0;
  while (x < list.length) {
    ls.unshift(list[x]);
    x++;
  }
  return ls;
};
