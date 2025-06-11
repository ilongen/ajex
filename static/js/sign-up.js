function  validateForm() {
    const user_email = document.getElementById('email').value;
    const user_password = document.getElementById('password').value;
    const user_name = document.getElementById('username').value
    const user_confirm = document.getElementById('confirm').value;

    // VALIDATED IS NULL
    if (user_email !== "" && user_password !== "" && user_confirm !== "") {
        alert("Values is null")
    }
    if (user_name !== "") {
        alert("User name is null")
    }
    if (user_confirm !== "") {
        alert("E-mail Confirm is null")
    }
    if (user_email !== ""){
        alert("Email is null")
    }
    if (user_password !== ""){
        alert("Password is null")
    }
}



async function data_singup() {
    validateForm();

    let url_post = 'http://localhost:8000/api/v1/users/signup'
    await fetch(url_post, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
    })
}
}