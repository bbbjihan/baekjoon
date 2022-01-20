const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let casecnt = Number(input.shift());
let stack =[];
let number = Array.from({length:casecnt},(e,i)=>i+1);
let result = '';
let wanvalue = [];
input.forEach(c=>{wanvalue.push(Number(c))});

for(var i=0; i<casecnt; i++){
    	var count = 1;
        while(count <= casecnt && stack[stack.length-1] != wanvalue[i]){
            stack.push(number.shift());
            result += '+\n';
            count++;
        }
    if(stack[stack.length-1] == wanvalue[i]){
        stack.pop();
        result += '-\n';
    }else{
        result = 'NO';
        break;
    }
}

console.log(result);