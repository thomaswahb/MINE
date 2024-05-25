let names = ["ali", "mhmd", "abdo", "gamal"];

console.log(names);
names.unshift("mahmoud");
console.log(names);
names.push("mai");
console.log(names);
let first = names.shift();
console.log(`my name is ${first}`);
let last = names.pop();

console.log(`my name is ${last}`);
