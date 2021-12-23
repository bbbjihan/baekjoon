const fs = require('fs');
const input = Number(fs.readFileSync('input.txt').toString().trim());

let fact = 1;
for(let i = 1; i<=input; i++){
    fact = fact * i;
}
console.log(fact);