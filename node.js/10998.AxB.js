const fs = require('fs');
const input = fs.readFileSync(0,'utf8').split(' ');

console.log(parseInt(input[0]) * parseInt(input[1]));