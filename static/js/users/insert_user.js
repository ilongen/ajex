const showNotification = (message, type = 'error') => {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type} show`;
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 5000);
};

const validateForm = (formData) => {
    const { username, password, email, email_confirm} = formData;
    
    if (!username || !password || !email || !email_confirm) {
        showNotification('Please fill in all required fields.');
        return false;
    }

    if (email !== email_confirm) {
        showNotification('Emails do not match.');
        return false;
    }

    if (username.length < 3 || username.length > 20) {
        showNotification('Username must be between 3 and 20 characters.');
        return false;
    }

    if (password.length < 6) {
        showNotification('Password must be at least 6 characters long.');
        return false;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showNotification('Please enter a valid email address.');
        return false;
    }

    return true;
};


const handleSignup = async () => {
    const formData = {
        username: document.getElementById('username').value.trim(),
        password: document.getElementById('password').value.trim(),
        email: document.getElementById('email').value.trim(),
        email_confirm: document.getElementById('email_confirm').value.trim()
    };

    if (!validateForm(formData)) {
        return;
    }

    const url = 'http://127.0.0.1:8000/api/v1/users/signup';

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify({
                username: formData.username,
                password: formData.password,
                email: formData.email
            })
        });

        const result = await response.json();

        if (!response.ok) {
            if (result.detail && result.detail.includes('auth_user_username_key')) {
                showNotification('This username is already taken. Please choose another.');
            } else {
                showNotification(result.message || 'Account creation failed. The username or email you provided is already in use. Please update your information and try again.');
            }
            return;
        }

        showNotification('Account created successfully! Redirecting...', 'success');
        setTimeout(() => {
            window.location.href = '/pages/sign-in';
        }, 2000);
    } catch (error) {
        showNotification('Connection error: Unable to reach the server. Please check your internet connection.');
        console.error('Signup error:', error);
    }
};