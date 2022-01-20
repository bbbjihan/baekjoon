const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

console.log(Math.min(Number(input[0]),Number(input[1]),Math.abs(Number(input[0])-Number(input[2])),Math.abs(Number(input[1])-Number(input[3]))));