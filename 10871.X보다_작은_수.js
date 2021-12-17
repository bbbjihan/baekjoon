const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let std = input[0].split(' ')[1];
let arr = [];

input[1].split(' ').forEach(c=>{
  if(Number(c)<Number(std))arr.push(c);
})

console.log(arr.join(' '));