//1
let age = 20
let hasID = true

if (age > 18 && hasID){
    console.log("Access allowed")
} else{
    console.log("Access denied")
}

//2

let username = "admin"
let password = 1234

if (username == "admin" && password == 1234){
    console.log("Login successful")
} else{
    console.log("Login failed")
}

//3

let number = 9

if (number > 0 && number < 10){
    console.log("Between 0 and 10")
} else{
    console.log("Out of range")
}

//4

let score = 60

if (score > 50 && score < 100){
    console.log("Passed")
} else{
    console.log("Failed")
}

//5

let hour = 11

if (hour > 9 && hour < 18){
    console.log("Working hours")
} else{
    console.log("Off hours")
}

//6

let ages = 8
let ticket = true

if (age < 12 || age < 60){
    console.log("Discount")
}

if (ticket && age < 12 || age < 60){
    console.log("Normal entry")
}else{
    console.log("No entry")
}

//7

let  temp

if (temp > 30 || temp < 0){
    console.log("extreme weather")
}else{
    console.log("normal weather")
}
