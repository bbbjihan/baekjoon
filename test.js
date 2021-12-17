const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let tarcnt = Number(input[0]);
let tar = input[1].trim().split(' ');
let fincnt = Number(input[2]);
let fin = input[3].trim().split(' ');

let result = '';
let value = '0\n';

for(let i = 0;i<fincnt;i++){
    for(let j=0;j<tarcnt;j++){
        if(fin[i]==tar[j]) value = '1\n';
    }
    result+=value;
    value = '0\n';
}

console.log(result);