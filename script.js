function showAbout() {
  document.getElementById("title").textContent = "About Me";
  document.getElementById("description").textContent = "Hello! My name is Kriman, and it's my first year at iFp! I'm recently 14 and I'm originated from Nepal.";
}

function showSkills() {
  document.getElementById("title").textContent = "Skills";
  document.getElementById("description").textContent = "I'm a decently fast learner, and understand how some things work with ease.";
}

function showExperience() {
    document.getElementById("title").textContent = "Experience";
    document.getElementById("description").textContent = "I have little experience coding on html, js, and css. However, I have coded on other sites and other languages.";
}

function showInterests() {
  document.getElementById("title").textContent = "Interests";
  document.getElementById("description").textContent = "I like coding, game design, 2d design, and more.";
}

function showiFrame() {
  this.toggleiframe();
}

function toggleiframe() {
  document.getElementById("iframe").style.display = this.iframe.style.display === 'block' ? 'none' : 'block';
}