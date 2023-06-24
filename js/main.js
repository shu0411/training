let message = "BINGO!";
const input = require('fs').readFileSync('/dev/stdin', 'utf8')
let n = parseInt(input, 10);
for (let i = 0; i < n; i++) {
    console.log(message);
}