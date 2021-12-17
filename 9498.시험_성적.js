const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());
let str = '';

if(input>59){
  if(input>69){
    if(input>79){
      if(input>89){
        str = 'A';
      }
      else{str = 'B';}
    }
    else{str = 'C';}
  }
  else{str = 'D';}
}
else{str = 'F';}

console.log(str);