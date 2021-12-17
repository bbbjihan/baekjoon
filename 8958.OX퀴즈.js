const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let casecnt = Number(input[0]);

for (let i = 1; i<=casecnt; i++){
  let ox = input[i].split('');
  let cnt = 0;
  let sum = 0;
  ox.forEach((c,i)=>{
    if(c == 'O') {cnt++;sum+=cnt;}
    else{cnt=0;}
  })
  console.log(sum);
}