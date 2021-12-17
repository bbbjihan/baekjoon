const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
let value = parseInt(input[0])*parseInt(input[1])*parseInt(input[2]);
let cnt = [0,0,0,0,0,0,0,0,0,0]

value.toString().split('').forEach(c=>{
    cnt[parseInt(c)]++;
})

cnt.forEach(c=>{
    console.log(c);
})