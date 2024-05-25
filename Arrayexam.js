let zero = 0;
let counter = 3;
let my = ["Ahmed", "Mazero", "Elham", "osama", "gamal", "Ameer"];
// here when i wanne increase a number without write number
console.log(my.slice(++zero, counter).reverse());

console.log(my[1][4] + my[1][5].toUpperCase());

console.log(my[2].slice(0, 2) + my[1].slice(2));

console.log(my.splice(++counter, --counter));
console.log(my.reverse());
