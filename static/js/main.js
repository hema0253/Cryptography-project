// Main JavaScript file for Network Security Analysis

document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add animation to cards
    const cards = document.querySelectorAll('.card');
    
    function checkIfInView() {
        cards.forEach(card => {
            const rect = card.getBoundingClientRect();
            const isInViewport = (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
            
            if (isInViewport && !card.classList.contains('animated')) {
                card.classList.add('animated');
                card.style.opacity = '1';
            }
        });
    }
    
    // Initialize cards with 0 opacity
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transition = 'opacity 0.5s ease-in-out, transform 0.3s ease';
    });
    
    // Check if cards are in view on load and scroll
    window.addEventListener('load', checkIfInView);
    window.addEventListener('scroll', checkIfInView);
    
    // Add active class to current nav item
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
});