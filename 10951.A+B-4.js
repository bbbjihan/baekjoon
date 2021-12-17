const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.forEach(c =>{
  console.log(Number(c.split(' ')[0]) + Number(c.split(' ')[1]));
})