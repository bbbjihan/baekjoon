const input = require("fs").readFileSync("input.txt").toString().trim();
const n = parseInt(input);

for (let i = 0; i < n; i++) {
  console.log(`${" ".repeat(i)}${"*".repeat(n - i)}`);
}
