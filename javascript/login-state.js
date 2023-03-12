fetch("/isloggedin", { 
    method: 'GET'
  })
      .then(function(response) { 
        var loginBtn = document.getElementById("login-btn");
        if (response == "true") {
            loginBtn.textContent = "Logout";
        }
        else {
            loginBtn.textContent = "Login";
        }
       });