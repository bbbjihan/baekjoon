const input = require("fs").readFileSync("input.txt").toString().trim();
const n = parseInt(input);

for (let i = 0; i < n; i++) {
  console.log(`${" ".repeat(n - i - 1)}${"*".repeat(2 * i + 1)}`);
}
