const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('');

let alpha = Array.from({length: 26}, () => -1);
input.forEach((c,i)=>{
  if(alpha[c.charCodeAt()-97] == -1){
    alpha[c.charCodeAt()-97] = i;
  }
})

alpha = alpha.join(' ');
console.log(alpha);