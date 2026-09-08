(function () {
  const scriptPath = "talking-button/script.js";
  const stylePath = "talking-button/style.css";
  const rootId = "chatbot-root";

  if (!document.querySelector('link[href="' + stylePath + '"]')) {
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = stylePath;
    document.head.appendChild(link);
  }

  let root = document.getElementById(rootId);
  if (!root) {
    root = document.createElement("div");
    root.id = rootId;
    document.body.appendChild(root);
  }

  if (!root.querySelector(".talking-button")) {
    root.innerHTML = `
      <button class="talking-button" onclick="openDialog()">💬</button>
      <div class="dialog-box" id="dialog-box">
        <p>Need some help?</p>
        <button onclick="showOptionOne()">Option 1</button>
        <button onclick="showOptionTwo()">Option 2</button>
        <button onclick="showOptionThree()">Option 3</button>
        <p id="response">Choose an option.</p>
      </div>
    `;
  }

  window.openDialog = function () {
    const dialogBox = document.getElementById("dialog-box");

    if (dialogBox.style.display === "block") {
      dialogBox.style.display = "none";
    } else {
      dialogBox.style.display = "block";
    }
  };

  window.showOptionOne = function () {
    document.getElementById("response").textContent = "Try one small step first.";
  };

  window.showOptionTwo = function () {
    document.getElementById("response").textContent = "You can use CSS to make it look cool.";
  };

  window.showOptionThree = function () {
    document.getElementById("response").textContent = "Keep practicing and you will improve.";
  };
})();
