let a = 10;

if (a < 10) {
  console.log(10);
} else if (a >= 10 && a <= 40) {
  console.log("10 to 40");
} else if (a > 40) {
  console.log("> 40");
} else {
  console.log("unknown");
}

a < 10
  ? console.log(10)
  : a >= 10 && a <= 40
  ? console.log("10 to 40")
  : a > 40
  ? console.log("> 40")
  : console.log("unknown");

let st = "Elzero Web School";

if ((st.length * 2).toString() === "34") {
  console.log("Good");
}

let second = function () {
  for (i in st) {
    if (st[i].toLocaleLowerCase() == "w") {
      let s = "w";
      return s;
    }
  }
};
// here i compare betwen 3 things (value , type and length)
if (st.length !== "string") {
  console.log("good");
}

if (typeof st.length === "number") {
  console.log("good");
}

if (st.slice(0, 6) + st.slice(0, 6) === "ElzeroElzero") {
  console.log("good");
}
