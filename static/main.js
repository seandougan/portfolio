const svgPath = document.querySelectorAll('.path');

const svgText = anime({
  targets: svgPath,
  loop: false,
  direction: 'alternate',
  strokeDashoffset: [anime.setDashoffset, 0],
  easing: 'easeInOutSine',
  duration: 900,
  delay: (el, i) => { return i * 50 }
});
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll(".navbar-nav .nav-item");

    navLinks.forEach(function(navLink) {
        navLink.addEventListener("click", function() {
            // Remove 'active' class from all nav items
            navLinks.forEach(function(link) {
                link.classList.remove("active");
            });

            // Add 'active' class to the clicked nav item
            navLink.classList.add("active");
        });
    });
});