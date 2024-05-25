let products = ["keyboard", "mouse", "pen", "pad", "monitor", "iphone"];
let color = ["green", "red", "blue"];

let show = 3;

document.write(`<h1> show ${show} product</h1>`);

for (let i = 0; i < show; i++) {
  document.write(`<div>`);
  document.write(`<h3>[${i + 1}] ${products[i]} </h3>`);

  for (let j = 0; j < color.length; j++) {
    document.write(`<p> ${color[j]} </p>`);
  }

  document.write(`</div`);
}
