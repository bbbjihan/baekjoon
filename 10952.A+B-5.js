const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for(let i = 0; i<input.length-1; i++){
  console.log(Number(input[i].split(' ')[0]) + Number(input[i].split(' ')[1]));
}