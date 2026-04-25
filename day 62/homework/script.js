let age = 18;
let hasPermission = true;

if (age >= 16 && hasPermission == true) {
    console.log("Can drive");
} else {
    console.log("Cannot drive");
}


let email = "user@gmail.com";
let password = "1234";

if ((email == "user@gmail.com" || email == "admin@gmail.com") && password == "1234") {
    console.log("Login success");
} else {
    console.log("Login failed");
}

let num = 50;

if (num >= 1 && num <= 100) {
    console.log("In range");
} else if (num < 1 || num > 100) {
    console.log("Out of range");
}


let isOnline = true;
let battery = 15;

if (isOnline == true && battery > 20) {
    console.log("Device ready");
} else if (isOnline == true && battery <= 20) {
    console.log("Low battery");
} else {
    console.log("Offline");
}


let weather = "sunny";
let temperature = 22;

if (weather == "sunny" && temperature >= 25) {
    console.log("Go outside");
} else if (weather == "rainy" || temperature < 10) {
    console.log("Stay home");
} else {
    console.log("Maybe go out");
}
