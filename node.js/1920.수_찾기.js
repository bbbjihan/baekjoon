const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let tarcnt = Number(input[0]);
let tar = input[1].split(' ').map(x=>Number(x));
const set = new Set(tar);
tar = [...set].sort((a,b)=>{
    return a-b;
});

let fincnt = Number(input[2]);
let fin = input[3].split(' ');
let result = '';
let finft = 0;

for(let i = 0; i < fincnt; i++){
    let low = 0;
    let high = tar.length-1;
    let mid = Math.floor((low+high)/2);
    while(low != high){
        if(tar[mid]<Number(fin[i])){low = mid+1}
        else if(tar[mid]>Number(fin[i])){high = mid-1}
        else{break;}
        mid = Math.floor((low+high)/2);
    }
    if(tar[mid]==Number(fin[i])){result+='1'}else{result+='0'}
}

console.log(result.split('').join('\n'));