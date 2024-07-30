
let scrollUp = document.querySelector('.scroll-up');
let scrollUpBar = document.getElementById('scroll-up-link');

scrollUp.addEventListener("click", function() {
    if (scrollUpBar.className == 'hide') {
        scrollUpBar.className = '';
    }
    else {
        scrollUpBar.className = 'hide';
    }
    });