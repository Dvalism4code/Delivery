var counter = 1;
setInterval(function(){
  document.getElementById('radio' + counter).checked = true;
  counter++;
  if(counter > 4){
    counter = 1;
  }
}, 8000);

/* Toggle between adding and removing the "responsive" class to nav-bar 
when the user clicks on the icon */

function myFunction() {
  var x = document.getElementById("top-nav");
  if(x.className === "nav-bar"){
    x.className += "responsive";
  }
  else{
    x.className = "nav-bar";
  }
}
/*
// FORM VALIDATION
function validateContactForm(event) {
  event.preventDefault(); // prevent the form submission if validation fails

  // Get the form field values
  var name = document.getElementsByClassName("name").value;
  var email = document.getElementsByClassName("email").value;
  var phone = document.getElementsByClassName("phone").value;
  var subject = document.getElementsByClassName("subject").value;
  var message = document.getElementsByClassName("message").value;

  // Perform validation
  if(name === ''){
    alert('this field is required');
    return false;
  }
  if(email === '') {
    alert("this field is required");
    return false;
  }
  if(phone === ''){
    alert('this field is required');
    return false;
  }
  if(subject === ''){
    alert('this field is required');
    return false;
  }
  if(message === ''){
    alert('this field is required');
    return false;
  }
  return true;
}

// validating the tracking code
function validateTrackForm(event) {
  event.preventDefault();

  var unique = {
    id: '{{ tracking.unique_id }}',
  };
  var form = document.getElementsByClassName("input").value;
  if(form === ''){
    alert('enter a tracking code');
    return false;
  }
  if(form != unique[id]){
    alert('enter a valid tracking id');
    return false;
  }
  return true;
}
*/
// validating the uuid
// In your HTML file or JavaScript code



    // Function to validate a UUID
    function isValidUUID(uuid) {
      var uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
      return uuidPattern.test(uuid);
    }

    // Function to handle form submission
    function handleSubmit(event) {
      event.preventDefault();

      var uuidInput = document.getElementById('uuidInput');
      var uuidValue = uuidInput.value;

      if (isValidUUID(uuidValue)) {
        console.log('Valid UUID:', uuidValue);
        // Add your code here to handle the valid UUID, such as sending it to the server
        // You can make an AJAX request or submit the form to the server using the appropriate method
        document.getElementById('myForm').submit(); // Example: submitting the form
      } 
      else {
        console.log('Invalid UUID:', uuidValue);
        // Add your code here to handle the invalid UUID, such as displaying an error message to the user
        uuidInput.value = ''; // Clear the entered value
        uuidInput.placeholder = 'Enter a valid tracking ID'; // Set the error message as the placeholder
        uuidInput.classList.add('error'); // Add the error class to the input for red outline
      }
    }

