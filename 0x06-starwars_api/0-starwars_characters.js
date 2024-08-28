#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const chars = JSON.parse(body).characters;
  exactOrder(chars, 0);
});

const exactOrder = (chars, x) => {
  if (x === chars.length) return;
  request(chars[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(chars, x + 1);
  });
};
