const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const casecnt = Number(input.shift());

for(let i = 0; i<casecnt; i++){
    a = Number(input[i].split(' ')[0]);
    b = Number(input[i].split(' ')[1]);
    console.log('Case #'+ (i+1).toString() +': '+(a+b).toString());
}