const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let A = Number(input[0].split('').reverse().join(''));
let B = Number(input[1].split('').reverse().join(''));

console.log(A>B? A : B);