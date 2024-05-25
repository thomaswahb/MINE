// document.write("<h1>hello</h1>");

// window.alert("hello from js");

// console.log("hello from js")

// console.table(["ali", "mhmd", "amr"])

// console.error("it is error");

// console.log(typeof("ali mhmd"));

// console.log("hi every \"one\"");

// let a = "we";
// let b = "love javaScript";
// let c = "And";
// let d = "programming";
// console.log(a + " " + b + " " + c + " " + d)

// console.log(`${a} ${b} ${c} ${d}`)

// let title = "Arab 4 pro";
// let dec = "4 programming";

// let desgin = `
//     <div class="do">
//         <div class="card">
//         <h1>${title}</h1>
//         <p>${dec}</p>

//         </div>
//     </div>
// `;

// document.write(desgin);

// في السطر دا لما احب اخلي كل المتغيرات في صف واحد
let TheTitle = "Elzero",
  Thedecs = "Elzero Web School",
  TheDate = "25/10";

let main = `
    <div class="card">
    <h3>Hello  ${TheTitle}</h3>

    <p>${Thedecs}</P>
    <span>${TheDate}</span>

    </div>
`;

document.write(main.repeat(4));
// دي طريقة اخري لكتابةالارقام في الجافا سكربت بحيث اني بكتب الواحد و بعد كدا الاي و معناها البرنامج يكتب كام صفر بعد الواحد
// console.log(1e3);

// console.log(100..toString());

// console.log(100.555.toFixed(2))

// let a = 1_00;
// let b = 2_00.5;
// let c = 1e2;
// let d = 2.4;

// let x = Math.min(1_00, 2_00.5, 1e2, 2.4)

// console.log(Math.round(x));

// console.log(Math.round(a) ** Math.floor(d));

// console.log(Math.round(d))
// console.log(Math.floor(d))
// console.log(parseInt(d))
// console.log(Math.trunc(d))

// console.log((parseInt(b) / Math.ceil(d)).toFixed(2))
// console.log(Math.round(parseInt(b)) / Math.ceil(d))

// console.log((Math.floor(b) / (Math.ceil(d))).toFixed(2)) // 66.67 String
// console.log(Math.ceil(b / (Math.ceil(d)))); // 67 Number

// function User(name, age) {
//   if (age < 20) {
//     console.log("this is app is not for you");
//   } else {
//     console.log(`welcome mr${name} your age is ${age}`);
//   }
// }

// User("mhmd", 23);
// User("mai", 18);
// User("ahmed", 27);

// function thisyear(start, end) {
//   for (i = start; i <= end; i++) {
//     console.log(i);
//   }
// }

// thisyear(1980, 2023);

// function year(start, end) {
//   for (i = 0; i <= end; i++) {
//     console.log(i);
//   }
// }
// year(2000, 2024);

console.log('Abdelwahab Gaber "Abdelwahab"');

console.log((100).toString());
console.log((1000.555).toFixed(2));
console.log(parseInt("100"));
console.log(parseFloat("100.500 abdo"));
console.log(Math.trunc(99.6));

let day = 5;

switch (day) {
  case 0:
    console.log("sat");
    break;
  case 1:
    console.log("sun");
    break;
  case 2:
    console.log("mon");
  default:
    console.log("unknown");
}

// for (let i = 0; i < 100; i++) {
// console.log(i);
// }
//let myfan = ["ali", "mhmd", "mai", "mia"];

for (let i = 0; i < myfan.length; i++) {
  console.log(myfan[i]);
}

let myfany = [1, 2, 5, "ali", "mhmd", "mai", "mia"];
let onlyname = [];
for (let i = 0; i < myfany.length; i++) {
  if (typeof myfany[i] === "string") {
    onlyname.push(myfany[i]);
  }
}

console.log(onlyname);
