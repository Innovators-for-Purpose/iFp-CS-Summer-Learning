function showAbout() {
  document.getElementById("Title").textContent="About Me";
  document.getElementById("Description").textContent="Hello! My name is Magan. I am an asipiring game developer who is interested in the story telling narrative aspect of games and the interesting complexities of game mechanics.";
  document.getElementById("Images").src= "../images/funky-cat.jpg"; 
  document.getElementById("Images").alt= "A Funny Cat Image";
}

function showSkills() {
  document.getElementById("Title").textContent = "Skills";
  document.getElementById("Description").innerHTML = "JavaScript<br>HTML<br>CSS<br>Python<br>";
  document.getElementById("Images").src= "../images/sneaky-cats.jpg";
  document.getElementById("Images").alt= "An Image Of Two Sneaky Cats";
}
function showExperience() {
  document.getElementById("Title").textContent = "Experience";
  document.getElementById("Description").textContent = "I have worked on projects with JavaScript and web design.";
  document.getElementById("Images").src= "../images/cat-pregnant.jpg";
  document.getElementById("Images").alt= "An Image Of A Pregnant Cat";
}

function showInterests() {
  document.getElementById("Title").textContent = "Interests";
  document.getElementById("Description").textContent = "I like coding, game design, and learning new tools.";
  document.getElementById("Images").src= "../images/burrito-cat.jpg";
  document.getElementById("Images").alt= "A Funny Cat Image where it's a burrito";
}

function showVideo() {
  document.getElementById("Title").textContent = "Cat Video";
  document.getElementById("Description").innerHTML = '<iframe width="400" height="400" src="https://www.youtube.com/embed/sXB6_Foueik?si=3Jd9kUL0MZzi1EaI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>';
}

function showGenius() {
  document.getElementById("Title").innerHTML = '<a style="color: inherit; text-decoration: inherit;" href="https://genius.innovatorsforpurpose.org/" target="_blank">Genius Project</a>';
  document.getElementById("Description").innerHTML = '<iframe width="400" height="400" src="https://genius.innovatorsforpurpose.org/" title="description"></iframe>';
}