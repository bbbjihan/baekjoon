const [N, M] = require("fs")
  .readFileSync("input.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const T = 2000001;

const isPrimes = new Array(T).fill(true);
isPrimes[0] = false;
isPrimes[1] = false;

for (let n = 2; n < T; n++) {
  const isPrime = isPrimes[n];
  if (!isPrime) continue;
  for (let i = n * 2; i < T; i += n) {
    isPrimes[i] = false;
  }
}

let success = false;
for (let i = 1; i < T; i++) {
  const seq = [];
  let now = i;
  for (let j = 0; j < N; j++) {
    if (isPrimes[now] || now > T) break;
    seq.push(now);
    now += M;
  }
  if (seq.length === N) {
    console.log(seq.join(" "));
    success = true;
    break;
  }
}
if (!success) console.log(-1);
