const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

const [N, K] = input[0].split(" ").map(Number);

for (let i = 0; i < N; i++) {
  const [G, X] = input[i + 1].split(" ").map(Number);
}
