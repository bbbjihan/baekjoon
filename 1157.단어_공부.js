const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().toUpperCase().split('');

let alpha = Array.from({length: 26}, () => 0);

input.forEach(c =>{
  alpha[c.charCodeAt()-65]++;
})

let max = 0;
let result = '';

for (let i = 0; i<26; i++){
   if (alpha[i] > max){
     max = alpha[i];
  }
}

if (alpha.indexOf(max) == alpha.lastIndexOf(max)){
  console.log(String.fromCharCode(alpha.indexOf(max)+65));
}
else{console.log("?");}