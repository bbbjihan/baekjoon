const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
let sum = 0;
input.forEach(c =>{
    sum = sum + (parseInt(c)*parseInt(c));
})
console.log(sum % 10);