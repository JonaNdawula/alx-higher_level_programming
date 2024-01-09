#!/usr/bin/node

exports.converter = function (base) {
  return function (a) {
    return parseInt(a, 10).toString(base);
  };
};
