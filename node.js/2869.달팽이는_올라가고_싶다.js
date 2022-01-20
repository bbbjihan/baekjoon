const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split(' ').map(Number);

console.log(parseInt((input[2]-input[1]-1)/(input[0]-input[1])+1));