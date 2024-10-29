const input = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split("\n");

for (let i = 0; i < Number(input[0]); i++) {
  const l = input[i * 2 + 2]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);

  let r = 0;
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 2; j < l.length; j++) {
      const [a, c] = [l[i], l[j]];
      if ((a + c) % 2) continue;
      const b = (a + c) / 2;

      let left = 0;
      let right = l.length - 1;
      while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (l[mid] == b) {
          r++;
          break;
        } else if (l[mid] > b) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }
    }
  }
  console.log(r);
}
