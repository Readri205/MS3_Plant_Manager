//Sends email from ontact form using EmalJS functionality
function sendMail(contactForm) {
  emailjs
    .send("gmail", "mtb_tours", {
      first_name: contactForm.first_name.value,
      last_name: contactForm.last_name.value,
      from_email: contactForm.email_address.value,
      contact_no: contactForm.contactno.value,
      message_text: contactForm.text.value,
    })
    .then(
      function (response) {
        console.log("SUCCESS", response);
      },
      function (error) {
        console.log("FAILED", error);
      }
    );
  return false; // To block from loading a new page
}

function myReset() {
  document.getElementById("myForm").reset();
}
$(document).ready(function () {
  $("form").submit(function () {
    alert(
      "Thanks! Your details have been submitted! Thanks for your time, comments and questions! We appreciate it!"
    );
  });
});
