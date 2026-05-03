window.app = {
    lightSwitchOn: false, 
    energySavingMode: false,
    enteringTheRoom: false, 
    standingOutside: true,
    leavingTheRoom: false,
    currentVideo: "data/v1.mp4", // Default video source

};
const app = window.app;
const videoSources = {
    v1_src : "data/v1.mp4", //standing outside, light off
    v2_src : "data/v2.mp4", //standing outside, light on
    v3_src : "data/v3.mp4", //entering room, light turns on
    v4_src : "data/v4.mp4", //entering room, light was on
    v5_src : "data/v5.mp4", //leaving room, light turns off (energy saving mode)
    v6_src : "data/v6.mp4", //leaving room, light stays on (normal mode, if switch is on)
}



const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => document.querySelectorAll(selector);
HTMLElement.prototype.on = function(event, handler) {
    this.addEventListener(event, handler);
    return this; // Enable chaining
};
HTMLElement.prototype.off = function(event, handler) {
    this.removeEventListener(event, handler);
    return this; // Enable chaining
};


const lightSwitchBtn = $("#light-switch-btn");
const energySavingSwitchBtn = $("#energy-saving-switch-btn");
const enterRoomBtn = $("#enter-room-btn");
const exitRoomBtn = $("#exit-room-btn");
const videoTag = $("#video-tag");
const navToggleBtn = $("#nav-toggle-btn");
const sideNav = document.querySelector('nav');

if (navToggleBtn && sideNav) {
    navToggleBtn.addEventListener('click', () => {
        sideNav.classList.toggle('hidden');
        // update aria attribute for accessibility
        const isHidden = sideNav.classList.contains('hidden');
        sideNav.setAttribute('aria-hidden', isHidden ? 'true' : 'false');
    });
}



lightSwitchBtn.on("click", () => {
    app.lightSwitchOn = !app.lightSwitchOn;
    const lamp = $("#light-lamp");
    if (app.lightSwitchOn) {
        lamp.classList.remove("lamp-off");
        lamp.classList.add("lamp-on");
    } else {
        lamp.classList.remove("lamp-on");
        lamp.classList.add("lamp-off");
    }
    renderVideo(); // Update video based on new state
});

energySavingSwitchBtn.on("click", () => {
    app.energySavingMode = !app.energySavingMode;
    const lamp = $("#energy-lamp");
    if (app.energySavingMode) {
        lamp.classList.remove("lamp-off");
        lamp.classList.add("lamp-on");
    } else {
        lamp.classList.remove("lamp-on");
        lamp.classList.add("lamp-off");
    }
    renderVideo(); // Update video based on new state
});

enterRoomBtn.on("click", () => {
    app.enteringTheRoom = true;
    app.standingOutside = false;
    app.leavingTheRoom = false;
    renderVideo(); // Update video based on new state
});

exitRoomBtn.on("click", () => {
    app.enteringTheRoom = false;
    app.standingOutside = false;
    app.leavingTheRoom = true;
    renderVideo(); // Update video based on new state
});

function inconsistentStateWarning() {
    console.warn("Inconsistent state detected. Defaulting to a safe video source.");
    updateVideoSource(videoSources.v1_src); // Default to standing outside, light off
}

function renderVideo() {
    if (app.enteringTheRoom) {
        if (app.energySavingMode){
            // If energy saving mode is on, show video where light turns on when entering the room
            updateVideoSource(videoSources.v3_src);
        } else if (app.lightSwitchOn) {
            //show video where light was on where entering the room
            updateVideoSource(videoSources.v4_src);
        } else {
            inconsistentStateWarning();
        }
    } else if (app.standingOutside) {
        // Outside idle state: light on => V2, otherwise V1.
        if (app.lightSwitchOn) {
            updateVideoSource(videoSources.v2_src);
        } else {
            updateVideoSource(videoSources.v1_src);
        }

    } else if (app.leavingTheRoom){
        //update video based on light switch status or energy saving mode, leave the room and then update the statuses and make standing outside true and render that video
        if (app.energySavingMode) {
            updateVideoSource(videoSources.v5_src);
        } else if (app.lightSwitchOn) {
            updateVideoSource(videoSources.v6_src);
        } else {
            inconsistentStateWarning();
        }
        // After showing the leaving video, reset to default state
        setTimeout(() => {
            app.leavingTheRoom = false;
            app.standingOutside = true;
            renderVideo(); // Render the standing outside video based on current switch states
        }, 5000); // Assuming each video is around 5 seconds long
    }
}

function updateVideoSource(src) {
    videoTag.src = src;
    videoTag.play();
    app.currentVideo = src; //should play once source is updated
}