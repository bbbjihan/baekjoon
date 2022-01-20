const fs = require('fs');
let input = fs.readFileSync("input.txt").toString().trim().split('\n').map(c=>c.split(' ').map(Number));

let cnt = input[0][1];
let length = input[0][0];
let array = input[1];
while(length!=0){
    let max = 0;
    let max_index = 0;
    for(let j = 0; j<length; j++){
        if(array[j]>max){max=array[j];max_index=j;}
    }
    if(array[length-1]<max){
        cnt--;
        if(cnt == 0){
            console.log(array[length-1].toString() + ' ' + array[max_index].toString());
            break;
        }
        [array[max_index],array[length-1]]=[array[length-1],array[max_index]];
    }
    length--;
}
if(length==0){console.log(-1)}