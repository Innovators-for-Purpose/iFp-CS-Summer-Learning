# iFp Summer Coding Practice

Welcome to iFp's summer coding practice! Over the next two weeks, you will learn to code in a more interactive way using a small webpage project.

## What You'll Do

- Work with JavaScript, HTML, and CSS
- Have hands-on practice editing your own customizable webpage

## What You'll Learn

This project will help you:

- Improve your JavaScript programming
- Understand HTML structure and content
- Style pages with CSS

## Your Next Step

By the time you finish, or when you feel you've made good progress, you can choose a project path to continue with:

- Game Development in Godot 3.5
- Web Development with JavaScript, CSS, and HTML
- AI Research and Development using Python


# Day 1-5

Navigate to VSCode in your applications and open the Summer Programming folder. In the folder, open the index.html, script.js, and style.css files. For this practice, you will be modifying these files, adding on to them, and making your very own webpage using this template. Each file will have their own objectives that you will complete in order to test you skills and help you learn how to code in this environment. 

There will be tips and definitions here to guide you and reference back if you feel unsure of what to do next. I also highly encourage you to make your own judgement and do your own research to help you, meaning you are able to use Google and other online resources like W3School to give you tips on how to code specific line. Your mentors will also be around to answer any questions you may have if you feel stuck or curious about a task.

## "index.html"

An HTML file is the main structure of a webpage. It uses tags to tell the browser what content should appear, such as headings, paragraphs, links, and images. In this practice, you will make a file is used to hold the page content and layout while the other files add style and behavior.



### Profile Card

1. Create a new file and name it `index.html`.
2. Open `index.html` in VS Code.
3. In the empty file, type `!` and press Tab or Enter to use Emmet. This will generate the basic HTML structure quickly.

Now time to create sections with `class` names so you can later different items to it later.

A `class` is a label you give to an HTML element. It helps you style that element with CSS and target it with JavaScript later.

To start, let's create start by adding a `div` into our body for a profile card class. You should end up with something that looks like this:

```html
<div class="profile-card">
</div>
```

`div` is a container that will hold content. We start it with `<div>` and end with `</div>`, where the `/` is indicating the end of the container. In this case we are having it hold the content of what we are calling out Profile Card. We can also more `div`'s inside another to help organize and structure our content. Lets make another `div` for a info box:

```html
<div class="info-box">
</div>
```

Now let's try adding it inside of the previous `div` for the Profile Card. Youll want to put it between the `<div class="profile-card">` and `</div`>. You should end up with something like this:

```html
<div class="profile-card">

    <div class="info-box">
    </div>

</div>
```
Because you are making a profile page, lets a container for buttons to change pages. Try it out on your own and add them within the Profile Card `div` as you did for the name box.

You should end up with something like this

<details>
  <summary>Click Show Answer</summary>
  
  Example structure for `home.html`:

    ```html
    <div class="profile-card">
        <div class="info-box">
        </div>
        <div class="buttons-container">
        </div>
    </div>
    ```

- `home-screen` is the main container for the whole page.
- `info-box` is for extra details or a short biography.
- `buttons-container` groups buttons like contact or portfolio links.

</details>


<br></br>

### Descriptions and Headings

Now add some words to our groups. We will be using the headings and paragraphs inside each section:

- Use `<h1>` for your name.
- Use `<p>` for your tagline and the info box text.
- Remember to use `<div>` to group each part of the page.

This makes your page easy to style and lets you later add content like a profile image, name, tagline, info box, and buttons container.

Let's add a name and tagline for our Profile Card group. To do this, we will use `<h1>` to add a line for our name and `<h3>` for our tagline

```html
<h1>Your Name Here</h1>
<h3> Your Title Here</h3>
```

And like the other groups we will add it within the '<div>':

```html

<div class="profile-card">
    <h1>Your Name Here</h1>
    <h3> Your Title Here</h3>
        <div class="info-box">
        </div>
        <div class="buttons-container">
        </div>
    </div>
```
Lets do the same for our info-box. Use `<h2>` to add a line for the title and `<p>` for our description. To make sure these are labeled, we will be adding `id`'s to them so we can modify them later. We adding an ID to a group, you add it within the starting `<...>` and set the id equal to `"..."`.

```html
<h2 id="Title">
    About Me
    </h1>
<p id="description"> 
    Your Title Here
    </p>
```

Now you have have this:

```html
<div class="profile-card">
    <h1>Your Name Here</h1>
    <h3> Your Title Here</h3>
        <div class="info-box">
            <h2 id="Title">
                About Me
                </h1>
            <p id="description"> 
                Your Title Here
                </p>
        </div>
        <div class="buttons-container">
        </div>
    </div>
```


### Images

Let's try adding an image to our page. We can call images and other files by using `src` to call for items in our directory. Because we are calling an image, we will use the `<img>` tag to call are image into. I have provided a folder called "Images", so for our source, we will have to take the path of where the photo is coming from before we call the image:

```html
src="images/profile_image.png"
```

Add the `<img>` tag into Profile-Card class, and put it right before your name tag. You should end up with something like this:

```html
<div class="profile-card">
    <img src="images/profile_image.png" alt="Profile Image">
    <h1>Your Name Here</h1>
    <h3> Your Title Here</h3>
        <div class="info-box">
            <h2 id="Title">
                About Me
                </h1>
            <p id="description"> 
                Your Title Here
                </p>
        </div>
        <div class="buttons-container">
        </div>
    </div>
```

### Buttons and Functions

Last, but not least, you will be adding buttons to your page. Because this will require scripting for them to work, we will only focus on adding the button itself to the page and do the functions in the Javascript section.

Just like images, buttons also have built-in tags for you to call the button and have it on your page. Try creating the tag yourself before you see how to do it below, make a button for your "About Me", and add it to the button-container class.


<details>
  <summary>Click Show Answer</summary>
  
  <button>About Me<button>

</details>

While we have the button tag made, we also need to assign it an "onclick" function. This will allow the button to be clickable. To do this, In the opening button tag add `onclick="...()"` and in the quotes tell it to show the about. You should end up with this:

```html
<button onclick="showAbout()">About Me<button>
```
Now add buttons for Skills, Interests, and Experience. Your html should look something like this:

<details>
  <summary>Click Show Answer</summary>

```html
<div class="profile-card">
    <img src="images/profile_image.png" alt="Profile Image">
    <h1>Your Name Here</h1>
    <h3> Your Title Here</h3>
        <div class="info-box">
            <h2 id="Title">
                About Me
                </h1>
            <p id="description"> 
                Your Title Here
                </p>
        </div>
        <div class="buttons-container">
            <button onclick="showAbout()">
                About Me
            </button>

            <button onclick="showSkills()">
                Skills
            </button>

            <button onclick="showExperience()">
                Experience
            </button>

            <button onclick="showInterests()">
                Interests
            </button>
        </div>
    </div>
```

</details>

Things to remember:
- The heading tag `<h1>` or `<h2>` changes the text inside it to a title for your page and the size of the heading.
- Add a paragraph using `<p>...</p>`
- Use a `<div>...</div>` container to group related content, like the title and paragraph.
- Remember that tags use angle brackets like `<tag>` to start and `</tag>` to end.


## "style.css"

A CSS file controls the look of your webpage. It changes how text, backgrounds, spacing, and layout appear so your HTML looks polished and easy to read.


1. Open `style.css` in VS Code. I have given you 3 empty,sections to start adding styles:

```css
.body{

},
.buttons-container {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 18px;
}

button {
  background-color: #5b7ff3;
  border: none;
  border-radius: 10px;
  color: white;
  cursor: pointer;
  padding: 12px 18px;
}

button:hover {
  background-color: #496fdb;
}
.
```


2. Add styles for the `body` so the page has a soft background and centered content.
3. Style `.profile-card`, `.info-box`, and `.buttons-container` so they have spacing, background color, and aligned text.
4. Use `color`, `background-color`, `padding`, `margin`, and `text-align`.

Example:

```css
body {
  background-color: #f4f7fb;
  color: #2e3a4f;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  display: flex;
  justify-content: center;
}

.profile-card {
  background-color: #ffffff;
  border-radius: 18px;
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.08);
  max-width: 460px;
  padding: 30px;
  text-align: center;
}

.info-box {
  background-color: #eef2fb;
  border-radius: 14px;
  margin: 20px 0;
  padding: 16px;
  text-align: left;
}

.buttons-container {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 18px;
}

button {
  background-color: #5b7ff3;
  border: none;
  border-radius: 10px;
  color: white;
  cursor: pointer;
  padding: 12px 18px;
}

button:hover {
  background-color: #496fdb;
}
```

This section is about using CSS to enhance your HTML file. Start with these styles, then adjust the colors, spacing, and alignment to make the page match your design.


## "script.js"

A JavaScript or sometimes refered to as JS file makes your page interactive. It controls behavior like updating text, responding to clicks, and changing content without reloading the page.


### How to write a function

A function is a block of code you can run by name. In JavaScript, a function looks like this:

```js
function showAbout() {
  // code to run when this function is called
}
```

Inside the function, you can change HTML content using `document.getElementById()`.

### What `document.getElementById()` means

- `document` is the web page.
- `getElementById()` finds one element by its `id` attribute.
- The code returns that element so you can change its text or style.

Example:

```js
document.getElementById("section-title").textContent = "About Me";
document.getElementById("description").textContent = "Hello! My name is ______.";
```

This finds the element with `id="section-title"` and replaces its text.

### Connecting functions to buttons

Buttons can call a function when clicked using `onclick="...()"`.

Example for HTML:

```html
<button onclick="showAbout()">About Me</button>
<button onclick="showSkills()">Skills</button>
<button onclick="showExperience()">Experience</button>
<button onclick="showInterests()">Interests</button>
```

Each button name should match the function name in `script.js`.


1. Open `script.js` in VS Code.
2. Add a function for each button you want to use.
3. Use `document.getElementById("description").textContent = "...";` to change the info text.
4. Make sure your buttons in `index.html` use `onclick="functionName()"`.

Example functions:

```js
function showExperience() {
  document.getElementById("section-title").textContent = "Experience";
  document.getElementById("description").textContent = "I have worked on projects with JavaScript and web design.";
}

function showInterests() {
  document.getElementById("section-title").textContent = "Interests";
  document.getElementById("description").textContent = "I like coding, game design, and learning new tools.";
}
```

This makes your buttons work and updates the page content when the user clicks them.






