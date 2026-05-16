//1
function getSeason(month) {
  switch (month) {
    case 12:
    case 1:
    case 2:
      return "ზამთარი";

    case 3:
    case 4:
    case 5:
      return "გაზაფხული";

    case 6:
    case 7:
    case 8:
      return "ზაფხული";

    case 9:
    case 10:
    case 11:
      return "შემოდგომა";

    default:
      return "არასწორი თვე";
  }
}

console.log(getSeason(4));

//2
let operation = "+";

switch (operation) {
  case "+":
    console.log("მიმატება");
    break;

  case "-":
    console.log("გამოკლება");
    break;

  case "*":
    console.log("გამრავლება");
    break;

  case "/":
    console.log("გაყოფა");
    break;

  default:
    console.log("უცნობი ოპერაცია");
}

//3
function isAdult(age) {
  if (age >= 18) {
    return "სრულწლოვანი";
  } else {
    return "არასრულწლოვანი";
  }
}

console.log(isAdult(20));

function isAdultTernary(age) {
  return age >= 18 ? "სრულწლოვანი" : "არასრულწლოვანი";
}

console.log(isAdultTernary(15));

//4
function trafficLight(color) {
  switch (color) {
    case "red":
      return "გაჩერდი";

    case "yellow":
      return "მოემზადე";

    case "green":
      return "წადი";

    default:
      return "უცნობი ფერი";
  }
}

console.log(trafficLight("green"));

//5
function maxNumber(a, b) {
  if (a > b) {
    return a;
  } else if (b > a) {
    return b;
  } else {
    return "ტოლია";
  }
}

console.log(maxNumber(5, 9));