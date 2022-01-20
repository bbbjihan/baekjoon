const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('');
const N = input[0];

for(let i = 0; i<9; i++){
    let str = N + " * " + (i+1).toString() + " = " + (parseInt(N)*(i+1)).toString();
    console.log(str);
}