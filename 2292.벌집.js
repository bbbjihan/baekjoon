const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

let number = Number(input);
let n = 0;
while(number!=1){
    if(3*n*(n-1)+1<number && 3*n*(n+1)+1>=number){break;}
    n++;
}
console.log(n+1);