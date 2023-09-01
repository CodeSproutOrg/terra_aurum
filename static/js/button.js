let MobNavButton = document.getElementById('menu-button');
let header = document.getElementById('header');

MobNavButton.addEventListener('click', OpenMenu);

function OpenMenu() {
    header.classList.toggle("open");
}