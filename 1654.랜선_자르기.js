const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const first_line = input.shift().split(' ');

let lan_stock = Number(first_line[0]);
let lan_needs = Number(first_line[1]);

let max = 0;
input.forEach(c=>{
  max+=Number(c);
})
max = Math.floor(max/lan_needs);  //max 중간값 설정

let min = 1;
let mid = 1;
let result = 1;;

while(max>=min){
  let n = 0;

  mid = Math.floor((max+min)/2);

  input.forEach(c => {
    n += Math.floor(Number(c)/mid);
  })

  if(n<lan_needs){
    max = mid-1
  }else{
    result = mid
    min = mid+1            
  } 
}

console.log(result);