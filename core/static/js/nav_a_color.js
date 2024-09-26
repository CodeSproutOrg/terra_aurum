const currentPath = window.location.pathname;
let nav_link = document.getElementsByClassName('navbar-button');

if (currentPath === '/app/' || currentPath.includes('/app/events/')) {
    header.style.backgroundColor = "unset";
    for (let link of nav_link) {
        link.style.color = 'var(--main-color)';
    }
};
