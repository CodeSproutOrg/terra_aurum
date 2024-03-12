let mainEventsContainer = document.getElementById('main-events');
let events = document.getElementsByClassName('main-event');
let totalEvents = events.length;
let currentIndex = 0;

function undispay_elem(elem) {
    Array.from(elem.children).forEach(child => {
        child.style.display = 'none';
    });
};

function delete_first_elem() {
    let deleted_elem = events[0];
    undispay_elem(deleted_elem);
    deleted_elem.style.minWidth = 0;
    setTimeout(function () {
       mainEventsContainer.removeChild(mainEventsContainer.children[0]);
    }, 5000);
};

function generate_next_event() {
    let current_elem = events[0];
    let clone_elem = current_elem.cloneNode(true);
    mainEventsContainer.appendChild(clone_elem);
};

function start_events() {
    try {
        if (currentIndex != totalEvents - 1) {
            generate_next_event();
            delete_first_elem();
            currentIndex += 1;
        } else {
            currentIndex = 0
        }
    } catch (error) {
        console.log(error);
    };
}


if (totalEvents > 1) {
    setInterval(start_events, 8000);
};

/* Sidebar menu */
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
