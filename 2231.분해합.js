const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim())

length = input.toString().length;
sum_max = length * 9;
let result = 0;

for(let i = 1; i<=sum_max; i++){
  let con = input-i;
  let con_sum = 0;
  con.toString().split('').forEach(c=>{
    con_sum += Number(c);
  })
  if(con + con_sum == input){; result = con;}
}

console.log(result);
