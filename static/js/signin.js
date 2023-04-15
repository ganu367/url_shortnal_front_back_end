
function myPassowrd() {
    var passwordHideIcon = document.getElementById("hide-password-icon");
    var passwordShowIcon = document.getElementById("show-password-icon");
    var passwordInput = document.getElementById("pass");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        passwordShowIcon.style.display = "block"
        passwordHideIcon.style.display = "none"

    } else {
        passwordInput.type = "password";
        passwordShowIcon.style.display = "none"
        passwordHideIcon.style.display = "block"
    }
  }