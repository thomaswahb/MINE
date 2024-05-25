let a = 1_00;
let b = 2_00.5;
let c = 1e2;
let d = 2.4;
// to find rhe smallest value betwen [a, b, c, d]
console.log(Math.trunc(Math.min(a, b, c, d)));
//get int 4 from d with 4 muthous
console.log(Math.trunc(d));
console.log(Math.floor(d));
console.log(Math.round(d));
console.log(parseInt(d));
// to get 10000 from a + d
console.log(Math.pow(a, Math.trunc(d)));
// to get this output
console.log((Math.floor(b) / Math.ceil(d)).toFixed(2));
console.log(Math.ceil(b / Math.ceil(d))); // 67 Number
