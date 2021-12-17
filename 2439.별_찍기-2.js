const fs = require('fs');
const input = fs.readFileSync('/dev/stdin');
const n = parseInt(input);
let aster = "";
for(let i = 0; i < n; i++){
   aster = " ".repeat(n-i-1) + "*".repeat(i+1);
   console.log(aster);
}