const fs = require('fs');
let input = fs.readFileSync(0,'utf8').trim().split(' ');

console.log(input.filter(x => x != "").length);