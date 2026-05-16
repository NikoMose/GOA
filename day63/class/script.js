//1
let num = 10;


if (num % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}

// ternary
console.log(num % 2 === 0 ? "Even" : "Odd");



//2

//3


//4

let password = "admin123";

if (password === "admin123") {
    console.log("Access granted");
} else {
    console.log("Access denied");
}

//5

let age = 25;

if (age < 13) {
    console.log("Child");
} else if (age >= 13 && age <= 19) {
    console.log("Teen");
} else if (age >= 20 && age <= 59) {
    console.log("Adult");
} else {
    console.log("Senior");
}

//6

let isLoggedIn = true;
let isAdmin = false;

if (isLoggedIn && isAdmin) {
    console.log("Welcome Admin");
} else if (isLoggedIn) {
    console.log("Welcome User");
} else {
    console.log("Please log in");
}