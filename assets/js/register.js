
var currentTab = 0;
// Current tab is set to be the first tab (0)
showTab(currentTab);
function showTab(n) {
  // This function will display the specified tab of the form...
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  //... and fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //... and run a function that will display the correct step indicator:
  fixStepIndicator(n)
}

//document.getElementById("nextBtn").onclick = function() {nextprev(1)};
//document.getElementById("prevBtn").onclick = function() {nextprev(-1)};

function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");
  // Exit the function if any field in the current tab is invalid:
  if (n == 1 && !validateForm()) return false;
  // Hide the current tab:
  x[currentTab].style.display = "none";
  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;
  // if you have reached the end of the form...
  showTab(currentTab);
}

function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid; // return the valid status
}
function fixStepIndicator(n) {
  // This function removes the "active" class of all steps...
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {

    x[i].className = x[i].className.replace(" active", "");
    //x[i].className.style.position ="fixed";

  }
  //... and adds the "active" class to the current step:
  x[n].className += " active";
}


function nukes(){
		 pass_error = "";
		 pass11 = document.getElementById("pass1").value
		 pass22 = document.getElementById("pass2").value
		 var lowerCaseLetters = /[a-z]/g;
		 var upperCaseLetters = /[A-Z]/g;
		 var numbers = /[0-9]/g;

if(lowerCaseLetters.test(pass11)==false) {
	alert("A Lowercase letter is required.");
}
  // Validate capital letters

  if(upperCaseLetters.test(pass11)==false) {alert("A Uppercase letter is required.");
	return false;
  }
  // Validate numbers
if(numbers.test(pass11)==false) {
alert("A Number letter is required.");
return false;
}
  // Validate length
 if(pass11.length < 8) {
	alert("Minimum 8 Characters are required.");
return false;
}
  if(pass11 !== pass22){
alert("Passwords don't match.");
return false;
}

return true;
   }


function submits(){
	if(nukes() == true){
	alert("Submitted");
  document.getElementById("form2").submit();

	}
}
