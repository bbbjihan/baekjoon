const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split(' ');

let n1 = Number(input[0]);
let n2 = Number(input[1]);

function prime(num){
    if (num==1){return false;}
    if (num==2){return true;}
    for (let i = 2; i<=Math.floor(Math.sqrt(num)); i++){
        if(num%i==0){
            return false;
        }
    }
    return true;
}

for(let i = n1; i<=n2; i++){
    if(prime(i)){console.log(i);}
}