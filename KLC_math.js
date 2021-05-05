/**
*Capstone
*/

var wrong = 0;
var right = 9;
var total = 0;
var score = 0;

var maxValue = 1000;
var minValue = 1;

numA = 0;
numB = 0;

function randomNumbers() {
	numA = Math.floor(Math.random() * (maxValue - minValue)) + (minValue);
	numB = Math.floor(Math.random() * (maxValue - minValue)) + (minValue);
	
	if (numB > numA {
		var temp = numA;
		numA = numB;
		numB = temp;
	}
}

function addition() {
	if (document.quiz.math[0].checked) {
		maxValue = 10;
	}else if (document.quiz.math[1].checked) {
		maxValue = 50;
	}else {
		maxValue = 100;
		minValue = 50;
	}
	
	randomNumbers();
	total = numA + numB;
	answer = parseFloat(window.prompt(numA + "+" + numB + "=" + " "));
	points();
}

function subtraction() {
	if (document.quiz.math[0]) {
		maxValue = 10;
	} else if (document.quiz.math[1].checked) {
		maxValue = 50;
	} else {
		maxValue = 100
	}
	
	randomNumbers();
	
	total = numA - numB;
	answer = parseFloat(window.prompt(numA = "-" + numB + "=" + " "));
	points();
}

function checkAnswer() {
	if (right != 0 && wrong != 0) {
		score = ((right/right + wrong) * 10).toFixed(2) + "%";
		alert("Your score is: " + score + "%" + "<br>" + "correct answers \n" + wrong + "wrong answers");
	} else {
		alert("Please finish your quiz.");
	}
}

function points() {

    var diviasion = .01;

    if ((total + diviasion) >= answer && (total - diviasion) <= answer) {
        right++;
        txt = " Correct answer";
    }
    else {
        wrong++;
        txt = "I' am sorry! your answer" + answer + " is not right.The correct answer is: " + total;

    }

    score = (right / (right + wrong) * 100).toFixed(2) + "%";

    alert("Your score is:" + score + "\n" + right + " correct answers \n" + wrong + " wrong answers");

}
	
		
		
		
		
		
		