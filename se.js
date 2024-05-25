let a = "Elzero web school";
// to return Zero
console.log(a.charAt(2).toUpperCase() + a.slice(3, 6));
// to return H 8times
console.log(a.slice(13, 14).toUpperCase().repeat(8));
// to return [Elzero]
console.log(a.slice(0, 6).split());
// to return Elzero school
console.log(a.substr(0, 6) + a.substr(10, 16));
// to return elZERO WEB SCHOOL
console.log(
    a.slice(0, 1).toLowerCase() +
    a.slice(1, 16).toUpperCase() +
    a.slice(16, 17).toLocaleLowerCase()
);
