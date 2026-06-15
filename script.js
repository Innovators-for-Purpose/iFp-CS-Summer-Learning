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

    document.getElementById("description").textContent = "Hello! My name is ______.";

}

function showSkills() {

    document.getElementById("section-title").innerHTML =
        "Skills";

    document.getElementById("description").innerHTML =
        "Python<br>HTML<br>CSS<br>JavaScript";

}