var submit = document.querySelector("#submit-btn");
var select = document.querySelector("#wrapper-main > h1 > select");
var answer = document.querySelector("#wrapper-main > h2 > span");
var sideA = document.querySelector("#side-1");
var sideB = document.querySelector("#side-2");
var sideC = document.querySelector("#wrapper-main > h2 > em");

function noValues() {
  answer.innerHTML = "Put A and B Values";
  sideC.innerHTML = "Put A and B Values";
}

function noANumber() {
  answer.innerHTML = "Please enter numbers";
  sideC.innerHTML = "Please enter numbers";
}
function placeholder(side1, side2) {
  sideA.placeholder = `enter for side ${side1} `;
  sideB.placeholder = `enter for side  ${side2} `;
}

submit.addEventListener("click", function (e) {
  e.preventDefault();
  console.log("clicked");
  if (sideA.value && sideB.value) {
    var cSquared = Number(sideA.value) ** 2 + Number(sideB.value) ** 2;

    if (cSquared.toString().toLowerCase() != "nan") {
      answer.innerHTML = cSquared;
      sideC.innerHTML = Math.sqrt(cSquared);
    } else {
      noANumber();
    }
  } else {
    noValues();
  }
});

select.addEventListener("change", function () {
  sideA.value = "";
  sideB.value = "";

  if (select.value == "a^2 + b^2 = c^2") {
    placeholder("A", "B");

    submit.addEventListener("click", function (e) {
      e.preventDefault();
      console.log("clicked");
      if (sideA.value && sideB.value) {
        var cSquared = Number(sideA.value) ** 2 + Number(sideB.value) ** 2;

        if (cSquared.toString().toLowerCase() != "nan") {
          answer.innerHTML = cSquared;
          sideC.innerHTML = Math.sqrt(cSquared);
        } else {
          noANumber();
        }
      } else {
        noValues();
      }
    });
  }

  if (select.value == "a^2 - c^2 = b^2") {
    placeholder("A", "C");

    submit.addEventListener("click", function (e) {
      e.preventDefault();
      console.log("clicked");
      if (sideA.value && sideB.value) {
        var cSquared = Number(sideA.value) ** 2 - Number(sideB.value) ** 2;
        cSquared = Number(cSquared.toString().replace("-", ""));

        if (cSquared.toString().toLowerCase() != "nan") {
          answer.innerHTML = cSquared;
          sideC.innerHTML = Math.sqrt(cSquared);
        } else {
          noANumber();
        }
      } else {
        noValues();
      }
    });
  }

  if (select.value == "c^2 - b^2 = a^2") {
    placeholder("B", "C");

    submit.addEventListener("click", function (e) {
      e.preventDefault();
      console.log("clicked");
      if (sideA.value && sideB.value) {
        var cSquared = Number(sideB.value) ** 2 - Number(sideA.value) ** 2;
        cSquared = Number(cSquared.toString().replace("-", ""));

        if (cSquared.toString().toLowerCase() != "nan") {
          answer.innerHTML = cSquared;
          sideC.innerHTML = Math.sqrt(cSquared);
        } else {
          noANumber();
        }
      } else {
        noValues();
      }
    });
  }
});
