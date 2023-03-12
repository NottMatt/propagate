fetch("/is-logged-in", { 
    method: 'GET'
  })
      .then((response) => {response.json()})
      .then((data) => 
      {
        loginBtn = document.getElementById("login-btn");
      if (data == "true") {
        loginBtn.textContent = "Logout"
      }
      else {
        loginBtn.textContent = "Login"
      }});