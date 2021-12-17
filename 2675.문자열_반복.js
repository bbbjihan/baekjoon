const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = parseInt(input[0]);
for (let i = 0; i < T; i++){
    let S = input[i+1].split(' ')[1].split('');
    let R = parseInt(input[i+1].split(' ')[0]);
    let new_S = [];
    S.forEach(c =>{
        new_S.push(c.repeat(R));
    })
    console.log(new_S.join(''));
}