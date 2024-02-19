let MobNavButton = document.getElementById('menu-button');
let navbar = document.getElementById('nav-bar');
let header = document.getElementById('header');

MobNavButton.addEventListener('click', OpenMenu);
document.addEventListener('click', ClosedMenu);

function OpenMenu() {
    event.stopPropagation();
    navbar.classList.toggle("open");
    MobNavButton.classList.toggle("closed");
}
function ClosedMenu() {
    navbar.classList.toggle("open");
    MobNavButton.classList.toggle("closed");
}