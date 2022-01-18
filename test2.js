temp = [12345,123];

let test = temp.shift().toString().trim().split('').map(Number);

console.log(test);
console.log(temp);