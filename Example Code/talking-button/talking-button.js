class TalkingButton extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          margin-top: 24px;
        }

        .talking-button {
          width: 60px;
          height: 60px;
          border: none;
          border-radius: 50%;
          background-color: #5b7ff3;
          color: white;
          font-size: 24px;
          cursor: pointer;
        }

        .dialog-box {
          display: none;
          margin-top: 16px;
          padding: 16px;
          background-color: white;
          border-radius: 12px;
          box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
          max-width: 280px;
        }

        .dialog-box button {
          margin: 6px 6px 0 0;
          padding: 8px 10px;
          border: none;
          border-radius: 8px;
          background-color: #eef2ff;
          color: #213047;
          cursor: pointer;
        }

        #response {
          margin-top: 10px;
          font-weight: bold;
        }
      </style>
      <button class="talking-button">💬</button>
      <div class="dialog-box" id="dialog-box">
        <p>Need some help?</p>
        <button class="option" data-answer="Try one small step first.">Option 1</button>
        <button class="option" data-answer="You can use CSS to make it look cool.">Option 2</button>
        <button class="option" data-answer="Keep practicing and you will improve.">Option 3</button>
        <p id="response">Choose an option.</p>
      </div>
    `;

    this.button = this.shadowRoot.querySelector('.talking-button');
    this.dialog = this.shadowRoot.getElementById('dialog-box');
    this.response = this.shadowRoot.getElementById('response');
    this.options = this.shadowRoot.querySelectorAll('.option');

    this.button.addEventListener('click', () => this.toggleDialog());
    this.options.forEach((option) => {
      option.addEventListener('click', () => this.setResponse(option.dataset.answer));
    });
  }

  toggleDialog() {
    this.dialog.style.display = this.dialog.style.display === 'block' ? 'none' : 'block';
  }

  setResponse(text) {
    this.response.textContent = text;
  }
}

customElements.define('talking-button', TalkingButton);
