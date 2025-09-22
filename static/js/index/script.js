// Toggle search input visibility
const searchIcon = document.querySelector('.search-icon');
const searchInput = document.querySelector('.search-input');
const searchContainer = document.querySelector('.search-container');

searchIcon.addEventListener('click', (e) => {
    e.stopPropagation(); // Prevent click from bubbling to document
    searchInput.classList.toggle('show');
    if (searchInput.classList.contains('show')) {
        searchInput.focus();
    }
});

// Hide search input when clicking outside
document.addEventListener('click', (e) => {
    if (!searchContainer.contains(e.target)) {
        searchInput.classList.remove('show');
    }
});

// Prevent clicks inside search input from closing it
searchInput.addEventListener('click', (e) => {
    e.stopPropagation();
});

// Search functionality for partial matches
searchInput.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase();
    const items = document.querySelectorAll('.content-item');
    items.forEach(item => {
        const text = item.textContent.toLowerCase();
        item.style.display = text.includes(query) ? 'block' : 'none';
    });
});

// Toggle hamburger menu for mobile
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const authButtons = document.querySelector('.auth-buttons');
hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('show');
    authButtons.classList.toggle('show');
});