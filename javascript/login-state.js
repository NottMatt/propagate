fetch('/is-logged-in').then((response) => response.json()).then((data) => {
    loginBtn = document.getElementById("login-btn")
    loginBtn.textContent = data == true ? 'Logout' : 'Login'
})
