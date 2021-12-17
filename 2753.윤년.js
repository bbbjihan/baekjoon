const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

let a = Number(input);

if (a%4 == 0){
  if (a%100 ==0){
   if (a%400 == 0){ a = 1 }
   else { a = 0 }
  }
  else { a = 1 }
}
else{ a = 0 }

console.log(a);