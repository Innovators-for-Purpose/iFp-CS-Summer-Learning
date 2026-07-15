function showAbout() 
    {document.getElementById("title").textContent="Information";

    document.getElementById("description").textContent="Hello! My name is Nathan Yohannes. I am 14 and a new student at Ifp.";

     document.getElementById("img").src="images/IFP.png";
}


function showSkills() 
    {document.getElementById("title").textContent="My Skills";

    document.getElementById("description").textContent="I consider myself good at reading, and am currently learning how to code.";

    document.getElementById("img").src="images/Html.png";
}



function showExperience() 
    {document.getElementById("title").textContent="Experience";

    document.getElementById("description").textContent="When I was younger I had an interest in code and had taken a class but aside from that this is my first experience working with code.";
    
    document.getElementById("img").src="images/EXP.png";
}



function showInterests() 
    {document.getElementById("title").textContent="My Interests";

    document.getElementById("description").textContent="I am very interested in computer science aswell as building computers as those two are what I'm hoping to pursue in the future.";

     document.getElementById("img").src="images/CS.png";
    }


function showIframe(){
document.getElementById("title").textContent="Genius";
document.getElementById("description").textContent="Genius Within project by Ifp."
document.getElementById("img").src="images/Genius.png"

const frameBox = document.getElementById("iframe");

if (frameBox.style.display === "block") {
    frameBox.style.display = "none";
} else {
    frameBox.style.display = "block";
}

}


function showVideo(){

    document.getElementById("img").src="images/Play.png"
    document.getElementById("description").innerHTML = `<video width="320" height="240" controls>
            <source id="vid" src="videos/Vid.mp4" type="video/mp4">
        </video>`;

    document.getElementById("title").textContent="Video";


    //document.getElementById("vid").src="videos/Vid.mp4";


    video.style.display = 'block'; 
    
}
function openDialog(){
    document.getElementById("dialog-box").style.display= "block";
}

function showOptionOne(){
    document.getElementById("response").textContent = "This is Nathan Yohannes' (my) portfolio describing him.";
}

function showOptionTwo(){
    document.getElementById("response").textContent = "My career goals are pursuing computer science or engineering.";
}

function showOptionThree(){
    document.getElementById("response").textContent = "Ifp is an AI/coding/design internship for Cambridge student that is working to transform the future of AI for everyone.";

}

