// let job = "manger";
// let salary = 0;

// if (job === "manger") {
//   salary = 8000;
// } else if (job === "it" || job === "support") {
//   salary = 6000;
// } else if (job === "developer" || job === "desginer") {
//   salary = 7000;
// } else {
//   salary = 4000;
// }

let job = "manger";
let salary = 0;

switch (job) {
  case "manger":
    salary = 8000;
    console.log(`my money is ${salary}`);
    break;
  case "it":
  case "support":
    salary = 6000;
    console.log(`my money is ${salary}`);
    break;
  case "developer":
  case "desginer":
    salary = 7000;
    console.log(`my money is ${salary}`);
    break;
  default:
    console.log("unknown");
}
