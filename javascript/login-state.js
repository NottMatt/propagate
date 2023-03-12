fetch("/is-logged-in", { 
    method: 'GET'
  })
      .then(function(response) { 
        var loginBtn = document.getElementById("login-btn");
        console.log(response);
        if (response == "true") {
            loginBtn.textContent = "Logout";
        }
        else {
            loginBtn.textContent = "Login";
        }
       });