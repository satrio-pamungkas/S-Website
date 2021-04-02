function landingPageRedirect(identify) {
    let path = identify.id;

    if (path == "masuk") {
        window.location.href = "login.html";
    }
    else if (path == "daftar") {
        window.location.href = "register.html";
    }
}

function loginRedirect() {
    let correct = loginValidation();

    if (correct) {
        window.location.href = "home.html";
    } 
    else {
        alert("Username atau kata sandi salah");
    }
}

function registerRedirect() {
    let correct = registerValidation();

    if (correct) {
        alert("Berhasil membuat akun !");
    }
    else {
        alert("Harap isi form dengan benar");
    }
}

function loginValidation() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if ((username == "admin") && (password == "admin")) {
        return true;
    } 
        
    return false;

}

function registerValidation() {
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let password_repeat = document.getElementById("password-repeat").value;

    if ((username) && (email) && (password) && (password_repeat)) {
        return true;
    }

    return false;
}
