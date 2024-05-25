let a = 1_00;
let b = 2_00.5;
let c = 1e2;
let d = 2.4;

let x = Math.min(1_00, 2_00.5, 1e2, 2.4)

console.log(Math.round(x));

console.log(Math.round(a) ** Math.floor(d));

console.log(Math.round(d))
console.log(Math.floor(d))
console.log(parseInt(d))
console.log(Math.trunc(d))

console.log((parseInt(b) / Math.ceil(d)).toFixed(2))
console.log(Math.round(parseInt(b)) / Math.ceil(d))

console.log((Math.floor(b) / (Math.ceil(d))).toFixed(2)) // 66.67 String
console.log(Math.ceil(b / (Math.ceil(d)))); // 67 Number