const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n').map(c=>c.trim());

let cntnode = input.shift();

let value_array = [];
let leftptr_array = [];
let rightptr_array = [];

const create_node = (value,left,right) => { //노드생성
    value_array.push(value);
    leftptr_array.push(left);
    rightptr_array.push(right);
}

const create_tree = (array) =>{ //트리생성
    if(array.length==0){return;}
    let node = array.shift();
    create_node(node.split(' ')[0],node.split(' ')[1],node.split(' '))
    create_tree(input);
}

const preorder = () =>{ //전위순회
    
}

const inorder = () =>{  //중위순회

}

const postorder = () =>{    //후위순회

}

create_tree(input);
console.log(input);