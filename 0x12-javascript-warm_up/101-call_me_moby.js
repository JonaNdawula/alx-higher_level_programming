#!/usr/bin/node
exports.callMeMoby = function (number, funct) {
  for (let x = 0; x < number; x++) {
    funct();
  }
};
