const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split('\n');

let i = 0;
while(input[i] != '0 0 0'){
    a = Number(input[i].split(' ')[0])*Number(input[i].split(' ')[0]);
    b = Number(input[i].split(' ')[1])*Number(input[i].split(' ')[1]);
    c = Number(input[i].split(' ')[2])*Number(input[i].split(' ')[2]);
    if((a+b)==c || (a+c)==b || (b+c)==a){console.log('right')}else{console.log('wrong')};
    i++;
}