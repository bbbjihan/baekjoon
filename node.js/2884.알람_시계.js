const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let H = Number(input[0]);
let M = Number(input[1]);

if (H == 0 && M <45){
  H = 24;
}

M+=H*60-45;
H = Math.floor(M/60);
M-=H*60;

console.log(H.toString() + ' ' + M.toString());