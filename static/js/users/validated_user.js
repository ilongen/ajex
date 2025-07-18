document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const usernameInput = document.querySelector('#username');
    const passwordInput = document.querySelector('#password');

    // Function to create and display notifications
    function showNotification(message, type) {
        // Remove existing notifications
        const existingNotification = document.querySelector('.notification');
        if (existingNotification) {
            existingNotification.remove();
        }

        // Create new notification
        const notification = document.createElement('div');
        notification.classList.add('notification', type);
        notification.textContent = message;

        // Add to body
        document.body.appendChild(notification);

        // Show notification
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);

        // Remove after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => {
                notification.remove();
            }, 400); // Wait for opacity transition
        }, 3000);
    }

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent default form submission

        const usernameOrEmail = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        // Basic front-end validation
        if (!usernameOrEmail || !password) {
            showNotification('Please fill in all fields.', 'error');
            return;
        }

        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/users/signin', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username: usernameOrEmail,
                    password: password,
                }),
            });

            const data = await response.json();

            if (response.ok) {
                // Successful login
                showNotification(data.message || 'Login successful!', 'success');
                // Optional: redirect after success
                setTimeout(() => {
                    window.location.href = '/dashboard';
                }, 1000);
            } else {
                // Error from API
                showNotification(data.message || 'Login failed.', 'error');
            }
        } catch (error) {
            // Network or other error
            showNotification('Server connection error.', 'error');
            console.error('Request error:', error);
        }
    });
});