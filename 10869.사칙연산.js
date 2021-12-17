const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let a = Number(input[0]);
let b = Number(input[1]);

console.log(a+b);
console.log(a-b);
console.log(a*b);
console.log(Math.floor(a/b));
console.log(a%b);