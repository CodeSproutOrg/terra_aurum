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
    deleted_elem.style.margin = '5% 0px 0px 0px';
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
} else {
    let event = document.getElementsByClassName('main-event')[0]
    event.style.transform = 'translateX(0)';
};
