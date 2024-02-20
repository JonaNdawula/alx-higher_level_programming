#!/usr/bin/node
// A js script that computes the
// number of tasks completed by
// use id

const reqst = require('request');

reqst.get(process.argv[2], { json: true }, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const finishedTasks = {};
  body.forEach(function (task) {
    if (task.completed) {
      if (!finishedTasks[task.userId]) {
        finishedTasks[task.userId] = 1;
      } else {
        finishedTasks[task.userId] += 1;
      }
    }
  });
  console.log(finishedTasks);
});
