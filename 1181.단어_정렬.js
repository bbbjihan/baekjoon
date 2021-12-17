const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let array = [];
let cnt = input.shift();
input.sort();

for(let i = 0; i<51; i++){
input.forEach(c=>{
  if(array[array.length-1]!=c){
  if(c.length==i){array.push(c);}
  }
})
}

array.forEach(c=>{console.log(c);})