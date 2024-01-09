#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurrenceCount = 0;
  let x = 0;
  while (x < list.length) {
    if (list[x] === searchElement) {
	    occurrenceCount++;
  }
    x++;
  }
  return (occurrenceCount);
};
