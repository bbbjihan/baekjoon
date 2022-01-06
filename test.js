const fs = require('fs');
const input = fs.readFileSync("input.txt").toString().trim().split('\n');

const cnt = Number(input[0]);
const operand = input[1].split(' ').map(Number);
let operator = input[2].split(' ').map(Number); // add, sub, mul, div

let make = [];

