const fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin').toString().trim());

let num_ptr = 0;

while(input>0){
  num_ptr++;
  if(num_ptr.toString().includes('666')){input--;}
}

console.log(num_ptr);