const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let casecnt = Number(input.shift());
let result = '';
for(let i = 0; i<casecnt; i++){
  let height = Number(input[i].split(' ')[0]);
  let weight = Number(input[i].split(' ')[1]);
  let number = Number(input[i].split(' ')[2]);
  let YY = 0;
  let XX = 1;
  for(let j = 1; j<=number; j++){
    YY++;
    if (YY>height){YY=1;XX++;}
  }
  YY = YY.toString();
  XX = XX<10? '0'+XX.toString() : XX.toString();
  console.log(YY+XX);
}