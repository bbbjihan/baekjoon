const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const input_1 = parseInt(input[0]);
const input_2 = input[1].split(' ');
const new_score = [];
let max = 0;

for (let i = 0; i<input_1; i++){
    if (parseInt(input_2[i]) > max) max = parseInt(input_2[i]);
}

for (let i = 0; i<input_1; i++){
    new_score.push((parseInt(input_2[i])/max)*100);
}

let sum = 0;
for (let i = 0; i<input_1; i++){
    sum+=new_score[i];
}

console.log(sum / input_1);