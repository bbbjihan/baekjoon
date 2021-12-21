const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const casecnt = Number(input.shift());

let apart = Array.from({length:15},x=>Array.from({length:14},y=>0));
for(let i = 0; i<15; i++){
    for(let j = 0; j<14; j++){
        if(i==0){apart[i][j] = i+1}
        else if(j==0){apart[i][j] = 1}
        else{apart[i][j] = apart[i-1][j] + apart[i][j-1]}
    }
}
for(let i = 0;i<casecnt;i++){
    let k = Number(input[2*i]);
    let n = Number(input[2*i+1]);
    console.log(apart[k+1][n-1]);
}
