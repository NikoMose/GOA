function greet(firstname) {
    return "hello" + " " + firstname + "!"
}
console.log(greet("Niko"))


//2 -------------------------------------

function compare(a, b) {

    if (a > b) {

        console.log("a მეტია b-ზე")
    } else if (a == b) {
        console.log("a უდრის ბ-ს")
    } else {
        console.log("b მეტია a-ზე")
    }
}

//3 -----------------------------------------

function kelvintocelcius(kelvin) {
    return kelvin - 273.15
}

function farenheittocelcius(farenheit) {
    return (farenheit - 32) * (5 / 9)
}

console.log(kelvintocelcius(300))
console.log(farenheittocelcius(68))

//4 ----------------------------------------

function checkage(age) {
    if (age > 60) {
        console.log("user is senior")
    } else if (age >= 18){
        console.log("user is adult")
    } else {
        console.log("user is not adult")
    }
}

console.log(checkage(20))