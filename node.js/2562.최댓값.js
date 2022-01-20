const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let max = 0;
for(let i = 0; i<9; i++){
    if (parseInt(input[i])>max) max = parseInt(input[i]);
}
console.log(max);
console.log(input.indexOf(max.toString())+1);