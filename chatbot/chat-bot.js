class Chatbot extends HTMLElement {
    constructor () {
        super();
        this.attachShadow({ mode:'open' });
        this.shadowRoot.innerHTML = `
            <style>
                :host {
                    display:block;
                    margin-top: 24px;
                }
                .talking-button {
                    width: 60px;
                    height: 60px;
                    border: none;
                    border-radius: 50%;
                    background-color: #c38c1eff;
                    color: white;
                    font-size: 24px;
                    cursor: pointer;
                    }

                .dialogue {
                    display: none;
                    margin-top: 20px;
                    padding: 16px;
                    background-color: #e39a24;
                    border-radius: 12px;
                    box-shadow: 0 6px 20px rgba(24, 24, 24, 0.1);
                    max-width: 260px;
                    }

                button {
                    background-color: #9c6d00ff;
                    border: none;
                    border-radius: 10px;
                    color: white;
                    cursor: pointer;
                    padding: 12px 18px;
                    }

                button:hover {
                    background-color: #634809ff;
                    }
            </style>
        <button class="talking-button" onclick="openDialog()">
        💬</button>
        <div class="dialogue" id="dialogue">
            <p>Need some help?</p>
            <button class="option" data-answer="Well I am here to help you! To navigate through the UI, click the buttons in the middle and read the the text just above those buttons. Click a button to cycle through the text, you can click the button multiple times to go back to the text">Yes
            </button>
            <button class="option" data-answer="-">No
            </button>
            <button class="option" data-answer="image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwY_QtlAGubRj1MTL COx8TOufzD8ZeQwT6CvDqHT_sEI-b_3fKHJ9zTtm0&s=10, video: https://youtu.be/NnTycJg1MIo?si=JsrddXvAA4FFw2ZQ&t=6938">Image and Video Sources
            </button>
            <p id="response">Choose an option.</p>
        </div>
        `;

        this.button = this.shadowRoot.querySelector('.talking-button');
        this.dialogue = this.shadowRoot.getElementById('dialogue');
        this.response = this.shadowRoot.getElementById('response');
        this.options = this.shadowRoot.querySelectorAll('.option');

        this.button.addEventListener('click', () => this.toggleDialogue());
        this.options.forEach((option) => {
            option.addEventListener('click', () => this.setResponse(option.dataset.answer));
        });
    }

        toggleDialogue() {
            this.dialogue.style.display = this.dialogue.style.display === 'block' ? 'none' : 'block';
        }

        setResponse(text){
            this.response.textContent = text;
        }



    }
    customElements.define('chat-bot', Chatbot);