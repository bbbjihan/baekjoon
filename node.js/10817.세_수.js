const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split(' ').map(Number).sort((a,b)=>a-b);
console.log(input[1]);