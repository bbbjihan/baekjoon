const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let tarcnt = Number(input[0]);
let tar = input[1].split(' ').map(x=>Number(x));
const set = new Set(tar);
tar = [...set].sort((a,b)=>{
    return a-b;
});

let fincnt = Number(input[2]);
let fin = input[3];
let low = 0;
let high = tar.length-1;
let mid = Math.floor((low+high)/2);
let result = '';
let finft = 0;
console.log(mid);

for(let i = 0; i<fincnt; i++){
    low = 0;
    high = tar.length-1;
    mid = Math.floor((low+high)/2);
    finft = 0;
    while(low!=high){
        if(tar[mid]>fin[i]){high=mid}
        if(tar[mid]<fin[i]){low=mid}
        if(tar[mid]=fin[i]){finft = 1}
        mid = Math.floor((low+high)/2);
        console.log(mid);
        if(low+1 == mid && mid+1 == high){low = high;}
    }
    if(finft = 0){result+='0';}else{result+='1';}
}

console.log(result);