const fs = require("fs");
const input = fs.readFileSync("input.txt").toString();

const [a, b] = input.split(" ");

const getCoord = (num) => {
  return [(num - 1) % 4, Math.ceil(num / 4)];
};

const coordA = getCoord(a);
const coordB = getCoord(b);

console.log(Math.abs(coordA[0] - coordB[0]) + Math.abs(coordA[1] - coordB[1]));
