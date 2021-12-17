const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let max = Number(input[1].split(' ')[0]);
let min = Number(input[1].split(' ')[0]);

input[1].split(' ').forEach(c =>{
  if(Number(c)>max){max = Number(c);}
  if(Number(c)<min){min = Number(c);}
})

console.log(min.toString() + ' ' + max.toString());