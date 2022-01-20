const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let sum = 0;
input[1].toString().split('').forEach(c =>{
  sum+=Number(c);
})
console.log(sum);