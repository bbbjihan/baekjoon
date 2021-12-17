const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let arr = Array.from({length: 42},() => 0);

input.forEach(c =>{
  arr[Number(c)%42]++;
})

let result = arr.filter(x => x != 0).length;

console.log(result==0? 1: result);