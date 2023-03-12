fetch('/is-logged-in').then((response) => response.json()).then((data) => {
    var loginBtn = document.getElementById("login-btn")
    loginBtn.text = data == true ? 'Logout' : 'Login'
})
