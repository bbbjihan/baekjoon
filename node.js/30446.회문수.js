const input = require("fs").readFileSync("input.txt").toString().trim();
const n = parseInt(input);

const getNext = (now) => {
  let s = now.toString().split("");
  const l = s.length;

  let leftIndex = Math.floor((l - 1) / 2);
  let rightIndex = l - leftIndex - 1;

  let left = parseInt(s[leftIndex]);
  let right = parseInt(s[rightIndex]);

  while (left === 9) {
    s[leftIndex] = "0";
    s[rightIndex] = "0";
    if (leftIndex === 0) {
      s = ["1", ...s];
      s[s.length - 1] = "1";
      return parseInt(s.join(""));
    } else {
      leftIndex -= 1;
      rightIndex += 1;
    }
    left = parseInt(s[leftIndex]);
    right = parseInt(s[rightIndex]);
  }
  s[leftIndex] = (left + 1).toString();
  s[rightIndex] = (right + 1).toString();

  return parseInt(s.join(""));
};

let count = 0;
let now = 1;
while (1) {
  if (now > n) {
    break;
  }
  count += 1;
  now = getNext(now);
}
console.log(count);
