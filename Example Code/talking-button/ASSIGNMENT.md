# Assignment: Build a Small Talking Button (Clippy-like)

Goal: Create a small round icon that opens a mini-dialog with a phrase and 3 options; each option shows a single reply.

Files in this folder:
- `index.html` — demo page with the button and dialog markup.
- `style.css` — styles for the round icon and dialog.
- `script.js` — button behavior and option responses.

Step-by-step objectives

1) Inspect files
- Open `index.html`, `style.css`, and `script.js` to see the working demo.

2) Connect to your profile (optional)
- If you want the talking button on your own profile page, copy the HTML for the button and dialog from `index.html` into your `index.html` file inside your project, then copy `style.css` rules into your `style.css` (or import this stylesheet), and include `script.js` at the end of your `<body>`.

3) Read the HTML structure
- The button has `id="clippy-btn"` and the dialog is `id="clippy-dialog"`.
- The dialog contains a phrase, three `.option` buttons, and a `.response` area.

4) Styling task
- Tweak `style.css` to change colors, size, and the dialog position.
- Make the icon larger/smaller or put it on the left side.

5) Behavior task
- Open `script.js` and modify the `data-response` attributes on the three option buttons.
- Add a fourth option or change the phrase text in the dialog.

6) Accessibility task
- Ensure `aria-expanded` toggles correctly and the dialog has `aria-hidden` set.
- Try opening with keyboard (Tab → Enter) and closing with Escape.

7) Extend (challenge)
- Add a short animation when the dialog opens.
- Persist the last response in localStorage so it remains when reopened.
- Add a small voice using the Web Speech API (`speechSynthesis`) to read responses aloud.

Acceptance criteria
- The button opens a dialog with a phrase and 3 option buttons.
- Clicking an option displays its single-line response in the response area.
- Clicking outside or pressing Escape closes the dialog.
- Keyboard users can navigate to the icon and options and activate them.

Use this folder as a self-contained demo or copy pieces into your main profile project.
