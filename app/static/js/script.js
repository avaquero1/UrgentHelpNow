// Toggle the mobile navigation
const menuBtn = document.querySelector('.header__menu-btn');
const mobileNav = document.getElementById('mobileNav');

menuBtn.addEventListener('click', function() {
  mobileNav.classList.toggle('mobile-nav--open');
});
