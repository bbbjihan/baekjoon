const fs = require('fs');
const input = fs.readFileSync("input.txt").toString().trim().split('\n');

const cnt_jew = Number(input[0].split(' ')[0]);
const cnt_bag = Number(input[0].split(' ')[1]);
console.log('cnt_jew : ' + cnt_jew);
console.log('cnt_bag : ' + cnt_bag);

let arr_jew = input.slice(1,cnt_jew+1).map(c=>c.split(' ').map(Number));
let arr_bag = input.slice(cnt_jew+1,cnt_jew+cnt_bag+1).map(Number);

arr_jew.sort((a,b)=>{return b[1]==a[1] ? a[0]-b[0] : b[1]-a[1];});
arr_bag.sort((a,b)=>{return a-b;});

console.log('arr_jew : ' + arr_jew);
console.log('arr_bag : ' + arr_bag);

