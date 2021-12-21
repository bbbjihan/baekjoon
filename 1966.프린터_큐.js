const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

const casecnt = Number(input.shift());

let queue = [];
let tar = [];
let tarstock, tarindex;

function array_max(array){
    let max = array[0];
    array.forEach(c=>{
        if(max<c){max = c}
    })
    return max;
}

for(let i =0; i<casecnt; i++){
tarstock = Number(input[2*i].split(' ')[0])
tarindex = Number(input[2*i].split(' ')[1])
tar = input[2*i+1].split(' ').map(Number);
queue = [];

while(tar[0]!=array_max(tar) || tarindex != 0){
    if(tarindex==0){
        if(tar[0]==array_max(tar)){
            break;
        }
        else{
            tar.push(tar.shift())
            tarindex = tar.length;
        }
    }
    else{
        if(tar[0]==array_max(tar)){
            queue.push(tar.shift());
            tarindex--;
        }
        else{
            tar.push(tar.shift())
            tarindex--;
        }
    }
}
console.log(queue.length);
console.log(queue);
console.log(tar);
console.log('------');
}