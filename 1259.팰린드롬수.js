const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

input.splice(input.length-1,1);

function palin(str){
  let val = 0;
  let arr = str.split('');
  let cnt = Math.floor(arr.length/2)
    for(let i =0; i < cnt; i++){
      if(arr[i] != arr[arr.length-1-i]){val = 1;break;}
    }
    return val == 0? 'yes' : 'no';
}

input.forEach(c=>{
  console.log(palin(c));
})