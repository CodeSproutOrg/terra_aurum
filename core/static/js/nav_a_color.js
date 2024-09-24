let nav_link = document.getElementsByClassName('navbar-button')
const currentPath = window.location.pathname;


// Проверяем, на какой странице находимся
if (currentPath === '/app/') {
    for (let link of nav_link) {
        link.style.color = 'var(--main-color)';
    }
}