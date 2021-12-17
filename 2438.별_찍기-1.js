const fs = require('fs');
const input = fs.readFileSync('/dev/stdin');
const n = parseInt(input);
let aster = '*';

for(let i = 0; i < n; i++){
   console.log(aster);
   aster = aster + '*';
}
return 0;