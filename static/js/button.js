let MobNavButton = document.getElementById('menu-button');
let navbar = document.getElementById('nav-bar');
let header = document.getElementById('header');

MobNavButton.addEventListener('click', OpenMenu);
document.addEventListener('click', ClosedMenu);


let events = document.getElementsByClassName('main-event');
let totalEvents = events.length;
let currentIndex = 0;

setInterval(() => {
    try {
        if (currentIndex != 0 & currentIndex < totalEvents) {
            events[currentIndex - 1].style.transform = `translateX(${currentIndex * 100}%)`;
            events[currentIndex].style.transform = `translateX(-${currentIndex * 100}%)`;
        } else if (currentIndex == totalEvents) {
            events[currentIndex - 1].style.transform = `translateX(${currentIndex * 100}%)`;
            currentIndex = -1
        }
        currentIndex = (currentIndex + 1);
    } catch (error) {
        console.log("Content not exist" + error);
    };
}, 10000);



function OpenMenu() {
    event.stopPropagation();
    navbar.classList.toggle("open");
    MobNavButton.classList.toggle("closed");
}
function ClosedMenu() {
    navbar.classList.toggle("open");
    MobNavButton.classList.toggle("closed");
}
