// let i = 0;
// while (i < 10) {
// console.log(i);
// i++;
// }
function hello(user, age) {
  console.log(`hello ${user} your age is ${age}`);
}

hello("mhmd", 20);

function year(start, end, ex) {
  for (let i = start; i <= end; i++) {
    if (i === ex) {
      continue;
    }
    console.log(i);
  }
}
year(1980, 2024, 2000);
