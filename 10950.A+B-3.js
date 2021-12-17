const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let cnt = input[0];

for(let i = 1; i<=cnt; i++){
  console.log(Number(input[i].split(' ')[0])+Number(input[i].split(' ')[1]));
}

