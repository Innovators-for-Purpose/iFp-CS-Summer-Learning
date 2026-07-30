function showProjects() {
  document.getElementById("title").textContent = "Projects";
  document.getElementById("description").innerHTML = "I have been working with iFp during their summer sessions since 2024. In that time, I’ve worked on two main game projects: Uncover, a puzzle game set in a school where all the students have been hypnotized; and O.B.L.I.V.I.O.N., a 2D movement and combat platformer set in a dystopian city controlled by a malevolent AI.<br></br>For Uncover, I got to design and code one of the many puzzles - a color-matching cooking game where the goal is to intuit the right color for a drink recipe that will cure the students. You can try it for yourself here.<br></br>For O.B.L.I.V.I.O.N., I coded the movement mechanics for the main character, Alex, using a state machine system. This is a clip showing the core movement options - walking, running, jumping, crouching, and grappling.<br></br>I also worked on the dialogue system for the game, making sure to make each character feel different to speak to. This is a clip of a short demo conversation between Alex; his older sister, Avery; and their shared friend, Theo.<br></br>In terms of school projects, I built a robot as a part of my school’s Robotics STEMinar. It was meant to recreate the rocker-bogie movement style of the Curiosity mars rover.";
  document.getElementById("video").style.display = "none"
}

function showInterests() {
  document.getElementById("title").textContent = "Interests";
  document.getElementById("description").innerHTML = "I am very interested in coding and game design. I love playing all sorts of games, but my favorites are probably Minecraft, Stardew Valley, and Dungeons & Dragons. I also engage in visual arts, such as drawing and painting, and performing arts. I love playing the piano, drums, and the begena. I am a drama kid as well.<br></br>I also enjoy going out and being in nature. I garden and take regular walks around my town. I’m also on my school’s cross country team.";
  document.getElementById("video").style.display = "none"
}

function showAbout() {
  document.getElementById("title").textContent = "About Me";
  document.getElementById("description").innerHTML = "Hello! I’m an Ethiopian-American teenage girl who loves to create. Feel free to click around and see what I’ve worked on.";
  document.getElementById("video").style.display = "none"
}

function showSkills() {
  document.getElementById("title").textContent = "Skills";
  document.getElementById("description").innerHTML = "I am proficient in several coding languages, including HTML, CSS, JavaScript, Python, SQL, and GDScript. I am skilled with mechanics as well. In terms of design, I have used Canva and Adobe Illustrator for my work.<br></br>I have good leadership skills and work well with other people. I am also able to complete solo tasks efficiently. I am very adaptable and flexible with my work, and I am good at thinking outside of the box.";
  document.getElementById("video").style.display = "none"
}



function openDialogue() {
    const dialogBox = document.getElementById("dialog-box");
    if (dialogBox.style.display === "block") {
        dialogBox.style.display = "none";
    } else {
        dialogBox.style.display = "block";
    }
    const text = document.getElementById("answer-text")
    const linkedin = document.getElementById("linkedin")
    text.style.display = "none"
    linkedin.style.display = "none"
}

function showOptionOne() {
    const text = document.getElementById("answer-text")
    const link = document.getElementById("linkedin")
    link.style.display = "block"
    text.style.display = "none"
    /*if (text.style.display != "block") {
        text.style.display = "block";
    } else  {
        text.style.display = "none";
    }*/
}

function showOptionTwo() {
    const text = document.getElementById("answer-text")
    text.textContent = "My favorite drink is root beer!"
    const link = document.getElementById("linkedin")
    link.style.display = "none"
    text.style.display = "block"
     /*if (text.style.display != "block") {
        text.style.display = "block";
    } else  {
        text.style.display = "none";
    }*/
}

function showOptionThree() {
    const text = document.getElementById("answer-text")
    text.textContent = "I was able to code this site myself with the help of iFp’s portfolio tutorial! All of the styling was decided on by yours truly."
    text.style.display = "block"
    const link = document.getElementById("linkedin")
    link.style.display = "none"
    /* if (text.style.display != "block") {
        text.style.display = "block";
    } else  {
        text.style.display = "none";
    }*/
}