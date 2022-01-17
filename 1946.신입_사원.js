const fs = require('fs');
let input = fs.readFileSync("input.txt").toString().trim().split('\n');
let testcase = Number(input.shift());
input = input.map(c=>c.trim().split(' ').map(Number));
let cntindex = 0;

const audition = (index) =>{    //input 중 케이스 시작 index 받아서 출력하는 함수
    let applier = [];
    let cnt = Number(input[index].toString());
    for(let i = 0; i<cnt; i++){
        applier.push(input[index+i+1]);
    }
    applier.sort((a,b)=>{return a[0]-b[0];});
    //console.log(applier);
    applier.forEach((ele,idx)=>{
        let can = 0;
        for(let i = 0; i<idx; i++){
            if(ele[1]>applier[i][1]){can++;}
            //console.log('ele :'+ ele + ' 비교대상: ' + applier[i] + ' can: ' + can);
        }
        if (can != 0)cnt--;
    })
    console.log(cnt);
}

while(testcase!=0){
    audition(cntindex);
    cntindex+=input[cntindex][0]+1;
    testcase--;
}