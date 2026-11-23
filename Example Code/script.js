/* ========================================================
DEVELOPER PROFILE PROJECT

This website uses three files:

index.html: Controls the STRUCTURE
style.css: Controls the APPEARANCE
script.js: Controls the BEHAVIOR

Throughout the week, you will customize all three files
to build your own Developer Profile page.
======================================================== */


function showAbout() {

    document.getElementById("section-title").textContent = "About Me";

    document.getElementById("description").textContent = "Hello! My name is Bela!";

}

function showSkills() {

    document.getElementById("section-title").innerHTML = "Skills";

    document.getElementById("description").innerHTML =
        "Python<br>HTML<br>CSS<br>JavaScript";

}

function showExp() {

    document.getElementById("section-title").innerHTML = "Experience";

    document.getElementById("description").innerHTML = "Innovators for Purpose";

}

function showInterests() {
    document.getElementById("section-title").innerHTML = "Interests";
    document.getElementById("description").innerHTML = "Accessible design, AI literacy, Animation";

}

function showMessage(){
    document.getElementById("little-message").innerHTML = "Hey!";
}