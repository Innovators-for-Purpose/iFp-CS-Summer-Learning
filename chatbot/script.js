function openDialog() {
    const element = document.getElementById("dialog_box");
    if (element.style.display === "none") {
        element.style.display = "flex";
    }
    else {
        element.style.display = "none";
    }
}

function showOptionOne() {
    document.getElementById("response").textContent = "Option 1: Blah.";
}

function showOptionTwo() {
    document.getElementById("response").textContent = "Option 2: Brah.";
}

function showOptionThree() {
    document.getElementById("response").textContent = "Option 3: Bwah.";
}