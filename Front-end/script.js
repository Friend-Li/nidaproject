const sr = ScrollReveal ({
    distance: '65px',
    duration: 2600,
    delay: 450,
    reset: true
});

sr.reveal('.jewelery-text', {delay:200, origin:'top'});
sr.reveal('.jewelery-logo', {delay:450, origin:'top'});
sr.reveal('.icons', {delay:450, origin:'left'});

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
        
  



